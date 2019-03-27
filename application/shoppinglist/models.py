from application import db
from datetime import datetime

class Shoppinglist(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    total_price =  db.Column(db.Numeric(10,2))

    account_id = db.Column(db.Integer, db.ForeignKey('account.id', account_cascade='all, delete-orphan'),
                                                    nullable=False)

    def __init__(self):
        self.total_price = 0.0
