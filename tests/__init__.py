
# This is the __init__.py file for tests

# Importing necessary libraries
import unittest

# Importing test modules
from .test_order_processing import TestOrderProcessing
from .test_inventory_management import TestInventoryManagement
from .test_customer_support import TestCustomerSupport
from .test_decision_making import TestDecisionMaking
from .test_data_collection import TestDataCollection
from .test_data_preprocessing import TestDataPreprocessing
from .test_nlu import TestNLU
from .test_ml_model import TestMLModel
from .test_agent_actions import TestAgentActions

# Main function to run all tests
if __name__ == '__main__':
    unittest.main()
