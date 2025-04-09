import unittest
from src.data_processing.data_loader import load_data
from src.data_processing.preprocessor import preprocess_data

class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        self.file_path = 'data/soil_samples.csv'
        self.data = load_data(self.file_path)

    def test_data_loading(self):
        self.assertIsNotNone(self.data)
        self.assertGreater(len(self.data), 0)

    def test_data_preprocessing(self):
        processed_data = preprocess_data(self.data)
        self.assertIsNotNone(processed_data)
        self.assertGreater(len(processed_data), 0)
        self.assertIn('normalized_column', processed_data.columns)

if __name__ == '__main__':
    unittest.main()