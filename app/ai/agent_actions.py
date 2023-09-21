
from app.models import Order, Inventory, Customer

class AgentActions:
    def __init__(self):
        pass

    def process_order(self, order_id):
        order = Order.query.get(order_id)
        if order:
            order.status = 'Processing'
            return True
        return False

    def update_inventory(self, product_id, quantity):
        product = Inventory.query.get(product_id)
        if product:
            product.quantity += quantity
            return True
        return False

    def respond_to_customer(self, customer_id, message):
        customer = Customer.query.get(customer_id)
        if customer:
            customer.messages.append(message)
            return True
        return False
