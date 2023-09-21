
from app.models import inventory

class InventoryManagementService:
    def __init__(self):
        self.inventory = inventory.Inventory()

    def add_product(self, product):
        self.inventory.add_product(product)

    def remove_product(self, product):
        self.inventory.remove_product(product)

    def update_product(self, product):
        self.inventory.update_product(product)

    def get_product(self, product_id):
        return self.inventory.get_product(product_id)

    def get_all_products(self):
        return self.inventory.get_all_products()

    def check_stock(self, product_id):
        return self.inventory.check_stock(product_id)
