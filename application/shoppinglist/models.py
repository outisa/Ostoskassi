from application import db
from datetime import datetime

from sqlalchemy.sql import text

class Shoppinglist(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    name = db.Column(db.String(50), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                                                    nullable=False)

    products  = db.relationship("Shoppinglistproduct",
                     backref = db.backref('shoppinglist'), lazy=True)

    def __init__(self, name):
        self.name = name
        self.date = datetime.now()

    @staticmethod
    def shoppinglists_for_current_user(account=0):
        stmt = text("SELECT Shoppinglist.id, Shoppinglist.name FROM Shoppinglist"
                    " WHERE (account_id = :account)"
                    " ORDER BY Shoppinglist.date DESC").params(account=account)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response

    @staticmethod
    def shoppinglist_show_contents(list=0):
        stmt = text("SELECT Shoppinglist.id, Product.id, Product.name, Category.category, Product.price, Shoppinglistproduct.product_total,"
                    " (Shoppinglistproduct.product_total * Product.Price), (SELECT SUM(Shoppinglistproduct.product_total * Product.price) FROM shoppinglist "
                           "  JOIN Shoppinglistproduct ON Shoppinglistproduct.shoppinglist_id = Shoppinglist.id"
                           " JOIN Product ON Shoppinglistproduct.product_id = Product.id WHERE (Shoppinglist_id = :list)) FROM Shoppinglist"
                    " JOIN Shoppinglistproduct ON Shoppinglistproduct.shoppinglist_id = Shoppinglist.id"
                    " JOIN Product ON Shoppinglistproduct.product_id = Product.id"
                    " JOIN Category ON Product.category_id = Category.id"
                    " WHERE (Shoppinglist_id = :list) GROUP BY Shoppinglist.id, Product.id, Category.category, Product.price, Shoppinglistproduct.product_total"
                    " ORDER BY Category.category").params(list=list)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
           response.append({"list_id":row[0], "product_id":row[1], "name":row[2], "category":row[3], "price":row[4], "product_total":row[5], "in_total":row[6], "total":row[7]})

        return response

