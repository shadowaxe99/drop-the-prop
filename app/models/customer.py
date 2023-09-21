
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    orders = db.relationship('Order', backref='customer', lazy=True)

    def __init__(self, email, name):
        self.email = email
        self.name = name

    def __repr__(self):
        return '<Customer %r>' % self.email
