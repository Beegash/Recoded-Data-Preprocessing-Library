import pandas as pd

class DateTimeHandler:
    @staticmethod
    def to_datetime(df, column):
        """
        Converts a column in a DataFrame to datetime format.
        
        Args:
            df (pandas.DataFrame): The DataFrame containing the column to be converted.
            column (str): The name of the column to be converted.
            
        Returns:
            pandas.DataFrame: The DataFrame with the converted column.
        """
        df[column] = pd.to_datetime(df[column], errors='coerce')
        return df

    @staticmethod
    def extract_date_parts(df, column):
        """
        Extracts year, month, and day from a datetime column in a DataFrame.

        Args:
            df (pandas.DataFrame): The DataFrame containing the datetime column.
            column (str): The name of the datetime column.

        Returns:
            pandas.DataFrame: The DataFrame with additional columns for year, month, and day.

        """
        df[f'{column}_year'] = df[column].dt.year
        df[f'{column}_month'] = df[column].dt.month
        df[f'{column}_day'] = df[column].dt.day
        return df