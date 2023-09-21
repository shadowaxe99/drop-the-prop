
from sklearn.ensemble import RandomForestClassifier
from app.models import Order, Inventory, Customer
import pandas as pd

class DecisionMaker:
    def __init__(self):
        self.model = RandomForestClassifier()

    def train_model(self, X_train, y_train):
        self.model.fit(X_train, y_train)

    def make_decision(self, X):
        prediction = self.model.predict(X)
        return prediction

def get_training_data():
    orders = Order.query.all()
    inventories = Inventory.query.all()
    customers = Customer.query.all()

    df_orders = pd.DataFrame([order.to_dict() for order in orders])
    df_inventories = pd.DataFrame([inventory.to_dict() for inventory in inventories])
    df_customers = pd.DataFrame([customer.to_dict() for customer in customers])

    X_train = pd.concat([df_orders, df_inventories, df_customers], axis=1)
    y_train = df_orders['status']

    return X_train, y_train

def run_decision_maker():
    X_train, y_train = get_training_data()
    decision_maker = DecisionMaker()
    decision_maker.train_model(X_train, y_train)

    X_test = X_train.sample(5)
    decisions = decision_maker.make_decision(X_test)

    return decisions
