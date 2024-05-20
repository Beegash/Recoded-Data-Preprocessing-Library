import pandas as pd

class DataTypeConverter:
    @staticmethod
    def to_numeric(df, column):
        """
        Convert the values in a specific column of a DataFrame to numeric type.
        
        This method attempts to convert all values in the specified column to a numeric type. 
        Non-numeric values will be set as NaN.

        Parameters:
        df (pandas.DataFrame): The DataFrame containing the column to be converted.
        column (str): The name of the column to be converted.

        Returns:
        pandas.DataFrame: The DataFrame with the converted column.
        """
        df[column] = pd.to_numeric(df[column], errors='coerce')
        return df

    @staticmethod
    def to_categorical(df, column):
        """
        Convert a column in a DataFrame to categorical data type.
        
        This method changes the data type of the specified column to 'category', 
        which can help reduce memory usage and improve performance for categorical data.

        Parameters:
        df (pandas.DataFrame): The DataFrame containing the column to be converted.
        column (str): The name of the column to be converted.

        Returns:
        pandas.DataFrame: The DataFrame with the specified column converted to categorical data type.
        """
        df[column] = df[column].astype('category')
        return df
