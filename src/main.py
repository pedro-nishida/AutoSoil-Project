import os
import pandas as pd 
from data_processing.data_loader import load_data
from data_processing.preprocessor import preprocess_data
from analysis.soil_analyzer import analyze_soil
from analysis.ml_model import predict_fertilizer
from reports.report_generator import generate_report

def main():
    # Get absolute path to the data file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    data_path = os.path.join(project_root, 'data', 'soil_samples.csv')
    
    # Create output directory if it doesn't exist
    output_dir = os.path.join(project_root, 'reports')
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, 'soil_analysis_report.pdf')
    
    # Load soil data with absolute path
    data = load_data(data_path)
    print(f"Original columns: {data.columns.tolist()}")
    
    # Process the data once
    processed_data = preprocess_data(data)
    print(f"Processed columns: {processed_data.columns.tolist()}")
    
    # Run analysis and generate reports
    analysis_results = analyze_soil(processed_data)
    fertilizer_recommendations = predict_fertilizer(processed_data)
    generate_report(analysis_results, fertilizer_recommendations, output_file)

if __name__ == "__main__":
    main()