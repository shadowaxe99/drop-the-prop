
import unittest
from app.services.decision_making import DecisionMaker

class TestDecisionMaking(unittest.TestCase):

    def setUp(self):
        self.decision_maker = DecisionMaker()

    def test_make_decision(self):
        input_data = {"order_id": 1, "inventory_status": "In Stock", "customer_feedback": "Positive"}
        decision = self.decision_maker.make_decision(input_data)
        self.assertIsNotNone(decision)

    def test_invalid_input(self):
        input_data = {"order_id": None, "inventory_status": "In Stock", "customer_feedback": "Positive"}
        with self.assertRaises(ValueError):
            self.decision_maker.make_decision(input_data)

if __name__ == '__main__':
    unittest.main()
