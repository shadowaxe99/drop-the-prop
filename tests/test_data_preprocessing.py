
import unittest
from app.services.data_preprocessing import DataPreprocessor

class TestDataPreprocessing(unittest.TestCase):

    def setUp(self):
        self.preprocessor = DataPreprocessor()

    def test_preprocess(self):
        data = {"order_id": "123", "product": "Book", "quantity": "2", "price": "$20"}
        result = self.preprocessor.preprocess(data)
        expected = {"order_id": 123, "product": "Book", "quantity": 2, "price": 20.0}
        self.assertEqual(result, expected)

    def test_handle_missing_values(self):
        data = {"order_id": "123", "product": None, "quantity": "2", "price": "$20"}
        result = self.preprocessor.handle_missing_values(data)
        expected = {"order_id": 123, "product": "Unknown", "quantity": 2, "price": 20.0}
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
