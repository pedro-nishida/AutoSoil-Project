# src/analysis/ml_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import joblib

class SoilFertilityPredictor:
    def __init__(self, data):
        self.data = data
        self.model = RandomForestRegressor()

    def preprocess_data(self):
        # Assuming 'features' and 'target' are defined in the dataset
        X = self.data.drop(columns=['target'])
        y = self.data['target']
        return train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self):
        X_train, X_test, y_train, y_test = self.preprocess_data()
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        print(f'Model trained with MSE: {mse}')

    def save_model(self, filename='soil_fertility_model.pkl'):
        joblib.dump(self.model, filename)

    def load_model(self, filename='soil_fertility_model.pkl'):
        self.model = joblib.load(filename)

    def predict(self, new_data):
        return self.model.predict(new_data)
    
def predict_fertilizer(soil_params: pd.DataFrame) -> dict:
    """
    Predict fertilizer recommendations based on soil parameters.
    
    Args:
        soil_params (pd.DataFrame): Soil parameters including N, P, K, pH
        
    Returns:
        dict: Recommended fertilizer amounts and types
    """
    # Initialize default predictor if not already trained
    model_path = 'soil_fertility_model.pkl'
    try:
        predictor = SoilFertilityPredictor(soil_params)
        predictor.load_model(model_path)
    except FileNotFoundError:
        return {
            'error': 'Model not trained. Please train the model first.',
            'recommendations': None
        }

    try:
        # Make predictions
        predictions = predictor.predict(soil_params)
        
        # Convert predictions to recommendations
        recommendations = {
            'nitrogen_fertilizer': float(predictions[0]),
            'phosphorus_fertilizer': float(predictions[1]),
            'potassium_fertilizer': float(predictions[2]),
            'confidence_score': float(np.mean(predictor.model.feature_importances_))
        }
                
        return {
            'error': None,
            'recommendations': recommendations
        }
        
    except Exception as e:
        return {
            'error': f'Prediction error: {str(e)}',
            'recommendations': None
        }