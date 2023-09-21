
import unittest
from app.services.data_collection import DataCollector

class TestDataCollection(unittest.TestCase):

    def setUp(self):
        self.data_collector = DataCollector()

    def test_collect_order_data(self):
        order_data = self.data_collector.collect_order_data()
        self.assertIsNotNone(order_data)

    def test_collect_inventory_data(self):
        inventory_data = self.data_collector.collect_inventory_data()
        self.assertIsNotNone(inventory_data)

    def test_collect_customer_data(self):
        customer_data = self.data_collector.collect_customer_data()
        self.assertIsNotNone(customer_data)

if __name__ == '__main__':
    unittest.main()
