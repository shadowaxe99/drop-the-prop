
import unittest
from app.services.inventory_management import InventoryManagement

class TestInventoryManagement(unittest.TestCase):

    def setUp(self):
        self.inventory_management = InventoryManagement()

    def test_add_product(self):
        result = self.inventory_management.add_product('Product1', 100)
        self.assertEqual(result, 'Product added successfully')

    def test_remove_product(self):
        self.inventory_management.add_product('Product2', 50)
        result = self.inventory_management.remove_product('Product2')
        self.assertEqual(result, 'Product removed successfully')

    def test_update_product_quantity(self):
        self.inventory_management.add_product('Product3', 200)
        result = self.inventory_management.update_product_quantity('Product3', 150)
        self.assertEqual(result, 'Product quantity updated successfully')

    def test_get_product_quantity(self):
        self.inventory_management.add_product('Product4', 300)
        result = self.inventory_management.get_product_quantity('Product4')
        self.assertEqual(result, 300)

if __name__ == '__main__':
    unittest.main()
