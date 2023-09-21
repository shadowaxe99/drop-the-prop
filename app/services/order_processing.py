
from app.models import Order

class OrderProcessingService:
    def __init__(self):
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def process_orders(self):
        for order in self.orders:
            order.process()

    def get_orders(self):
        return self.orders

    def get_order(self, order_id):
        for order in self.orders:
            if order.id == order_id:
                return order
        return None

    def remove_order(self, order_id):
        self.orders = [order for order in self.orders if order.id != order_id]
