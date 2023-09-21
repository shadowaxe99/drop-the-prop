
import unittest
from app.ai.ml_model import MLModel

class TestMLModel(unittest.TestCase):

    def setUp(self):
        self.ml_model = MLModel()

    def test_train(self):
        data = {'features': [[1, 2, 3], [4, 5, 6]], 'labels': [0, 1]}
        self.ml_model.train(data)
        self.assertIsNotNone(self.ml_model.model)

    def test_predict(self):
        data = {'features': [[1, 2, 3], [4, 5, 6]], 'labels': [0, 1]}
        self.ml_model.train(data)
        predictions = self.ml_model.predict([[7, 8, 9]])
        self.assertIsNotNone(predictions)

    def test_save_model(self):
        data = {'features': [[1, 2, 3], [4, 5, 6]], 'labels': [0, 1]}
        self.ml_model.train(data)
        self.ml_model.save_model('test_model.pkl')
        self.assertTrue(os.path.exists('test_model.pkl'))

    def test_load_model(self):
        data = {'features': [[1, 2, 3], [4, 5, 6]], 'labels': [0, 1]}
        self.ml_model.train(data)
        self.ml_model.save_model('test_model.pkl')
        loaded_model = self.ml_model.load_model('test_model.pkl')
        self.assertEqual(self.ml_model.model, loaded_model)

if __name__ == '__main__':
    unittest.main()
