''''
Python file for custom functions used in project
'''
# Package dependencies
import numpy as np


def find_column_type(df):
    """
    This function identify categorical, boolean and numerical values.
    Parameters
    ---------
    df : DataFrame
        Usually a DataFrame with training samples that will be used to fit a model.
    Returns
    -------
    categorical_cols : list
        Categorical features.
    bool_cols:
        Boolean features.
    numerical_cols:
        Numerical features.
    """
    
    all_cols=list(df.columns)
    numerical_cols_temp = df._get_numeric_data().columns
    categorical_cols = list(set(all_cols) - set(numerical_cols_temp))
    bool_cols = [col for col in all_cols if np.isin(df[col].dropna().unique(), [0, 1,0.0,1.0]).all()]
    numerical_cols = list(set(numerical_cols_temp) - set(bool_cols))
    
    return categorical_cols,bool_cols,numerical_cols