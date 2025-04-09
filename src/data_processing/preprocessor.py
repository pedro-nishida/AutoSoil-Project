import pandas as pd
import numpy as np

def preprocess_data(df):
    """
    Preprocess the soil data.
    
    Args:
        df (pd.DataFrame): The input DataFrame containing soil data
        
    Returns:
        pd.DataFrame: Preprocessed data
    """
    # Data preprocessing steps
    # Example operations:
    # 1. Handle missing values
    df = df.fillna(df.mean(numeric_only=True))
    
    # 2. Normalize numeric columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())
    
    # 3. Other preprocessing steps as needed
    
    return df