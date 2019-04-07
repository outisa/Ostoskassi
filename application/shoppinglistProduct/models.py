from application import db
from sqlalchemy.sql import text

class Shoppinglistproduct(db.Model):
    shoppinglist_id = db.Column(db.Integer, db.ForeignKey('shoppinglist.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    product_total = db.Column(db.Integer, nullable=False)


    def __init__(self, total):
        self.product_total = total

    @staticmethod
    def update_product_total(amount=0, shoppinglist=0, product=0):
        stmt = text("UPDATE Shoppinglistproduct SET product_total= :amount"
               " WHERE (shoppinglist_id = :shoppinglist AND product_id = :product)").params(amount=amount, shoppinglist=shoppinglist, product=product)

        res = db.engine.execute(stmt)
