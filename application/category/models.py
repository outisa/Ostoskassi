from application import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    category = db.Column(db.String(150), nullable=True)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id', account_cascade='all, delete-orphan'),
                                                         nullable=False)

    products = db.relationship("Product", backref='category', lazy=True) 
    def __init__(self, category):
        self.category = category

