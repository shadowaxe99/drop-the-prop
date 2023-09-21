
import unittest
from app.services.customer_support import CustomerSupport

class TestCustomerSupport(unittest.TestCase):

    def setUp(self):
        self.customer_support = CustomerSupport()

    def test_handle_customer_query(self):
        query = "Where is my order?"
        response = self.customer_support.handle_customer_query(query)
        self.assertIsNotNone(response)

    def test_update_customer_info(self):
        customer_info = {"name": "John Doe", "email": "johndoe@example.com"}
        result = self.customer_support.update_customer_info(customer_info)
        self.assertTrue(result)

    def test_send_customer_notification(self):
        notification = "Your order has been shipped."
        result = self.customer_support.send_customer_notification(notification)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()

