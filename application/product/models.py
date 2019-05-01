from application import db

from sqlalchemy.sql import text

class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                                                               nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
                                                               nullable=False)

    products  = db.relationship("Shoppinglistproduct",
          backref=db.backref('product'), lazy=True)

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @staticmethod
    def list_products_user(account=0):
        stmt = text("SELECT Product.id, Product.name, Product.price, Category.category FROM Product"
               " JOIN Account ON Product.account_id = account.id"
               " JOIN Category ON Product.category_id = Category.id"
               " WHERE (Product.account_id = :account)"
               " ORDER BY Product.name").params(account=account)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "price":row[2], "category":row[3]})

        return response
