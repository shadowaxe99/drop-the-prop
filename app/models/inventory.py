
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Inventory(db.Model):
    __tablename__ = 'inventory'

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    product_sku = db.Column(db.String(50), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(100), nullable=False)

    def __init__(self, product_name, product_sku, quantity, location):
        self.product_name = product_name
        self.product_sku = product_sku
        self.quantity = quantity
        self.location = location

    def __repr__(self):
        return f'<Inventory {self.product_name}>'
