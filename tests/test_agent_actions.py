
import unittest
from app.ai.agent_actions import AgentActions

class TestAgentActions(unittest.TestCase):

    def setUp(self):
        self.agent_actions = AgentActions()

    def test_process_order(self):
        order_id = 1
        result = self.agent_actions.process_order(order_id)
        self.assertEqual(result, True)

    def test_update_inventory(self):
        product_id = 1
        quantity = 10
        result = self.agent_actions.update_inventory(product_id, quantity)
        self.assertEqual(result, True)

    def test_handle_customer_query(self):
        query = "Where is my order?"
        result = self.agent_actions.handle_customer_query(query)
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
