import unittest
from src.analysis.soil_analyzer import analyze_soil
from src.analysis.ml_model import predict_fertilizer

class TestSoilAnalysis(unittest.TestCase):

    def test_analyze_soil(self):
        # Sample input data
        sample_data = {
            'pH': 6.5,
            'N': 50,
            'P': 30,
            'K': 40
        }
        result = analyze_soil(sample_data)
        self.assertIsInstance(result, dict)
        self.assertIn('recommendations', result)

    def test_predict_fertilizer(self):
        # Sample input data for prediction
        sample_features = [[6.5, 50, 30, 40]]  # pH, N, P, K
        predicted_fertilizer = predict_fertilizer(sample_features)
        self.assertIsInstance(predicted_fertilizer, str)

if __name__ == '__main__':
    unittest.main()