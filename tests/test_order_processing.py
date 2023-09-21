
import unittest
from app.services import order_processing

class TestOrderProcessing(unittest.TestCase):

    def setUp(self):
        self.order_processor = order_processing.OrderProcessor()

    def test_process_order(self):
        order = {"id": 1, "items": [{"id": "item1", "quantity": 2}, {"id": "item2", "quantity": 1}]}
        result = self.order_processor.process_order(order)
        self.assertEqual(result, True)

    def test_cancel_order(self):
        order_id = 1
        result = self.order_processor.cancel_order(order_id)
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()

