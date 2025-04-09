import pandas as pd
import os

def create_sample_data():
    """Create a sample soil analysis dataset."""
    data = {
        'sample_id': [f'SOIL{str(i).zfill(3)}' for i in range(1, 11)],
        'ph_level': [6.5, 5.8, 7.2, 6.8, 5.5, 7.0, 6.2, 7.5, 6.0, 6.7],
        'organic_matter': [3.2, 2.8, 4.1, 3.5, 2.5, 3.8, 3.0, 4.5, 2.7, 3.4],
        'nitrogen': [45, 38, 52, 48, 35, 50, 42, 55, 40, 47],
        'phosphorus': [28, 22, 35, 30, 20, 32, 25, 38, 24, 29],
        'potassium': [180, 150, 220, 200, 140, 210, 170, 240, 160, 190],
        'calcium': [1200, 980, 1450, 1350, 850, 1400, 1100, 1500, 950, 1250],
        'magnesium': [240, 190, 280, 260, 170, 270, 220, 300, 200, 250],
        'sulfur': [12, 8, 15, 14, 7, 13, 10, 16, 9, 11],
        'depth_cm': [15, 20, 10, 25, 30, 20, 15, 10, 25, 20],
        'texture': ['clay loam', 'sandy loam', 'silt loam', 'clay', 'sandy', 
                   'loam', 'clay loam', 'silt', 'sandy loam', 'loam'],
        'collection_date': pd.date_range('2024-01-15', periods=10, freq='D')
    }
    
    df = pd.DataFrame(data)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(current_dir, 'data')
    os.makedirs(output_dir, exist_ok=True)
    
    output_file = 'soil_samples.csv'
    print(f"Saving file to: {os.path.abspath(output_file)}")  # Debug print
    
    df.to_csv(output_file, index=False, encoding='utf-8')
    return df


if __name__ == "__main__":
    df = create_sample_data()
    print("Sample data created successfully!")