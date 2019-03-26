from application import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    category = db.Column(db.String(150), nullable=False)

    def __init__(self, category):
        self.category = category
