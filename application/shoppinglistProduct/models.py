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

    @staticmethod
    def show_total_costs_per_category(account=0):
        stmt = text("SELECT DISTINCT Category.category, SUM(shoppinglistproduct.product_total * product.price) AS sum,"
                    " SUM(shoppinglistproduct.product_total * product.price) * 100 / (SELECT SUM(shoppinglistproduct.product_total * product.price) FROM Shoppinglist" 
                          " JOIN Shoppinglistproduct ON Shoppinglistproduct.shoppinglist_id = Shoppinglist.id"
                          " JOIN Product ON Shoppinglistproduct.product_id = product.id"
                          " JOIN account ON account.id = Shoppinglist.account_id"
                          " WHERE (Product.account_id = :account)) AS percent"
                    " FROM Shoppinglistproduct"
                    " JOIN Product ON Shoppinglistproduct.product_id = product.id"
                    " JOIN Shoppinglist ON Shoppinglistproduct.shoppinglist_id = Shoppinglist.id"
                    " JOIN account ON account.id = Product.account_id"
                    " JOIN Category ON Category.id = Product.category_id"
                    " WHERE (Product.account_id = :account) GROUP BY Category.category"
                    " ORDER BY sum DESC LIMIT 15").params(account=account)

        res = db.engine.execute(stmt)

        response = []

        for row in res:
            percentage = round(row[2], 2)
            response.append({"category":row[0], "sum":row[1], "percent":percentage})

        return response
