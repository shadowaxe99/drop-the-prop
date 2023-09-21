
import unittest

# Import test modules
from tests.test_order_processing import TestOrderProcessing
from tests.test_inventory_management import TestInventoryManagement
from tests.test_customer_support import TestCustomerSupport
from tests.test_decision_making import TestDecisionMaking
from tests.test_data_collection import TestDataCollection
from tests.test_data_preprocessing import TestDataPreprocessing
from tests.test_nlu import TestNLU
from tests.test_ml_model import TestMLModel
from tests.test_agent_actions import TestAgentActions

# Initialize test suite
test_suite = unittest.TestSuite()

# Add tests to the suite
test_suite.addTest(unittest.makeSuite(TestOrderProcessing))
test_suite.addTest(unittest.makeSuite(TestInventoryManagement))
test_suite.addTest(unittest.makeSuite(TestCustomerSupport))
test_suite.addTest(unittest.makeSuite(TestDecisionMaking))
test_suite.addTest(unittest.makeSuite(TestDataCollection))
test_suite.addTest(unittest.makeSuite(TestDataPreprocessing))
test_suite.addTest(unittest.makeSuite(TestNLU))
test_suite.addTest(unittest.makeSuite(TestMLModel))
test_suite.addTest(unittest.makeSuite(TestAgentActions))

# Run the tests
runner = unittest.TextTestRunner()
runner.run(test_suite)
