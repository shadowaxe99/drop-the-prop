
# data_collection.py

from app.models import Order, Inventory, Customer
import pandas as pd

class DataCollection:

    @staticmethod
    def collect_orders_data():
        orders = Order.query.all()
        orders_df = pd.DataFrame([order.to_dict() for order in orders])
        return orders_df

    @staticmethod
    def collect_inventory_data():
        inventory_items = Inventory.query.all()
        inventory_df = pd.DataFrame([item.to_dict() for item in inventory_items])
        return inventory_df

    @staticmethod
    def collect_customer_data():
        customers = Customer.query.all()
        customer_df = pd.DataFrame([customer.to_dict() for customer in customers])
        return customer_df
