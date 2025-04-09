import pandas as pd
from pathlib import Path
from typing import Union


def load_data(file_path: Union[str, Path]) -> pd.DataFrame:
    """
    Load soil analysis data from CSV or Excel file.
    
    Args:
        file_path (str or Path): Path to the data file
        
    Returns:
        pd.DataFrame: Loaded soil analysis data
        
    Raises:
        ValueError: If file format is not supported
    """
    file_path = Path(file_path)
    
    if file_path.suffix.lower() == '.csv':
        return pd.read_csv(file_path)
    elif file_path.suffix.lower() in ['.xlsx', '.xls']:
        return pd.read_excel(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_path.suffix}")


def validate_data(df: pd.DataFrame) -> bool:
    """
    Validate if the dataframe contains required soil analysis columns.
    
    Args:
        df (pd.DataFrame): Input dataframe to validate
        
    Returns:
        bool: True if valid, False otherwise
    """
    required_columns = ['N', 'P', 'K', 'pH']
    return all(col in df.columns for col in required_columns)