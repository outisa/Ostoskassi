from application import db

from sqlalchemy.sql import text

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    category = db.Column(db.String(100), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                                                         nullable=True)

    products = db.relationship("Product", backref=db.backref('category.id'), lazy=True)
    def __init__(self, category):
        self.category = category

    @staticmethod
    def list_categories_for_user(account=0):
        stmt = text("SELECT Category.id, category FROM Category"
                    " JOIN account ON Category.account_id = account.id "
                    " WHERE (Category.account_id = :account)"
                    " ORDER BY Category.category").params(account=account)
        res = db.engine.execute(stmt)


        response = []
        for row in res:
            response.append({"id":row[0], "category":row[1]})

        return response

