
from datetime import datetime
from app import db

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    quantity = db.Column(db.Integer)
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20))

    def __init__(self, customer_id, product_id, quantity):
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity
        self.status = 'Pending'

    def __repr__(self):
        return f'<Order {self.id}>'
