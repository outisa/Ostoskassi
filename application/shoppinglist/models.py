from application import db
from datetime import datetime

shoppinglistProduct = db.Table('shoppinglistProduct',
              db.Column('shoppinglist_id', db.Integer, db.ForeignKey('shoppinglist.id')),
              db.Column('product_id', db.Integer, db.ForeignKey('product.id')),
                   )



class Shoppinglist(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    total_price =  db.Column(db.Numeric(10,2))

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                                                    nullable=False)

    shoppinglistProduct = db.relationship('Product', secondary=shoppinglistProduct, lazy='subquery',
                        backref = db.backref('shoppinglists', lazy=True))
    def __init__(self):
        self.total_price = 0.0
