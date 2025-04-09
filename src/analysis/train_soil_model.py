import pandas as pd
from ml_model import SoilFertilityPredictor

def train_soil_model(data_path: str):
    """
    Train the soil fertility prediction model.
    
    Args:
        data_path (str): Path to training data CSV file
    """
    # Load training data
    # Expected columns: N, P, K, pH, target (fertilizer recommendations)
    training_data = pd.read_csv(data_path)
    
    # Initialize predictor
    predictor = SoilFertilityPredictor(training_data)
    
    # Train model
    predictor.train_model()
    
    # Save trained model
    predictor.save_model()
    print("Model trained and saved successfully!")

if __name__ == "__main__":
    # Example training data path
    data_path = "data/training_data.csv"
    train_soil_model(data_path)