import pandas as pd
import numpy as np

def analyze_soil(data):
    """
    Analyzes soil data and provides detailed assessment.
    
    Args:
        data (pd.DataFrame): Preprocessed soil data
        
    Returns:
        dict: Analysis results
    """
    # Map the actual column names to expected names
    column_mapping = {
        'ph_level': 'pH',
        'nitrogen': 'N',
        'phosphorus': 'P',
        'potassium': 'K'
    }
    
    results = {
        'soil_quality': 'Unknown',
        'metrics': {},
        'recommendations': []
    }
    
    # Calculate statistics for all available columns
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    results['metrics'] = {
        'mean_values': {col: data[col].mean() for col in numeric_cols},
        'std_values': {col: data[col].std() for col in numeric_cols}
        #make another calcula
    }
    
    # Add soil quality assessment based on pH level
    if 'ph_level' in data.columns:
        mean_ph = data['ph_level'].mean()
        results['metrics']['ph_mean'] = mean_ph
        
        if mean_ph < 5.5:
            results['soil_quality'] = 'Acidic'
            results['recommendations'].append('Consider adding lime to increase pH')
        elif mean_ph > 7.5:
            results['soil_quality'] = 'Alkaline'
            results['recommendations'].append('Consider adding sulfur to decrease pH')
        else:
            results['soil_quality'] = 'Neutral'
    
    # Add nutrient assessment
    if 'nitrogen' in data.columns:
        nitrogen_level = data['nitrogen'].mean()
        if nitrogen_level < 0.3:  # Example threshold
            results['recommendations'].append('Consider adding nitrogen-rich fertilizer')
    
    return results