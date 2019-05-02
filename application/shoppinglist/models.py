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
        stmt = text("SELECT Product.id, Product.name, Category.category, Product.price, Shoppinglistproduct.product_total,"
                    " (Shoppinglistproduct.product_total * Product.Price), (SELECT SUM(Shoppinglistproduct.product_total * Product.price) FROM Shoppinglistproduct "
                           " JOIN Product ON Shoppinglistproduct.product_id = Product.id WHERE (Shoppinglistproduct.shoppinglist_id = :list)) FROM Shoppinglistproduct"
                    " JOIN Product ON Shoppinglistproduct.product_id = Product.id"
                    " JOIN Category ON Product.category_id = Category.id"
                    " WHERE (Shoppinglistproduct.shoppinglist_id = :list) GROUP BY Product.id, Category.category, Product.price, Shoppinglistproduct.product_total"
                    " ORDER BY Category.category").params(list=list)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
           response.append({"product_id":row[0], "name":row[1], "category":row[2], "price":row[3], "product_total":row[4], "in_total":row[5], "total":row[6]})

        return response

