
import unittest
from app.ai.nlu import NLU

class TestNLU(unittest.TestCase):

    def setUp(self):
        self.nlu = NLU()

    def test_process_text(self):
        text = "Hello, I want to place an order"
        result = self.nlu.process_text(text)
        self.assertIsNotNone(result)

    def test_extract_entities(self):
        text = "I want to order 5 units of product X"
        entities = self.nlu.extract_entities(text)
        self.assertEqual(len(entities), 2)
        self.assertEqual(entities[0]['entity'], 'quantity')
        self.assertEqual(entities[1]['entity'], 'product')

    def test_classify_intent(self):
        text = "What is the status of my order?"
        intent = self.nlu.classify_intent(text)
        self.assertEqual(intent, 'order_status')

if __name__ == '__main__':
    unittest.main()
