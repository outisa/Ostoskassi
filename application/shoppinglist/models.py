from application import db
from datetime import datetime

from sqlalchemy.sql import text

class Shoppinglist(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    total_price =  db.Column(db.Numeric(10,2), nullable=True)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                                                    nullable=False)

    products  = db.relationship("Shoppinglistproduct", backref = db.backref("shoppinglist"))

    def __init__(self):
        self.total_price = 0.0
        self.date = db.func.current_timestamp()

    @staticmethod
    def shoppinglists_for_current_user(account=0):
        stmt = text("SELECT Shoppinglist.id, Shoppinglist.date FROM Shoppinglist"
                    " JOIN Account ON Shoppinglist.account_id = Account.id"
                    " WHERE (account_id = :account)").params(account=account)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "date":row[1]})

        return response

    @staticmethod
    def shoppinglist_show_contents(list=0):
        stmt = text("SELECT Shoppinglist.id, Product.id, Product.name, Category.category, Product.price, ShoppinglistProduct.product_total,"
                    " Shoppinglist.total_price FROM Shoppinglist"
                    " JOIN ShoppinglistProduct ON ShoppinglistProduct.shoppinglist_id = Shoppinglist.id"
                    " JOIN Product ON ShoppinglistProduct.product_id = Product.id"
                    " JOIN Category ON Product.category_id = Category.id"
                    " WHERE (Shoppinglist.id = :list)").params(list=list)

        res = db.engine.execute(stmt)

        response = []
        for row in res:
           response.append({"list.id":row[0], "product.id":row[1], "name":row[2], "category":row[3], "price":row[4], "product_total":row[5], "total_price":row[6]})

        return response
