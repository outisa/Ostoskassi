from application import db

class Product(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id', 
                                    account_cascade='all, delete-orphan'),
                                                                  nullable=False)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
                                                               nullable=False)

    def __init__(self, name, price):
        self.name = name
        self.price = price
