import pandas as pd

class MissingValueHandler:
    @staticmethod
    def impute_mean(df, column):
        """
        Imputes missing values in a DataFrame column with the mean value of the column.

        This method fills missing values in the specified column using the mean of that column.

        Parameters:
        - df (pandas.DataFrame): The DataFrame containing the column to be imputed.
        - column (str): The name of the column to be imputed.

        Returns:
        - pandas.DataFrame: The DataFrame with the imputed column.
        """
        df[column] = df[column].fillna(df[column].mean())
        return df

    @staticmethod
    def impute_median(df, column):
        """
        Imputes missing values in a specific column of a DataFrame with the median value of that column.

        This method fills missing values in the specified column using the median of that column.

        Parameters:
            df (pandas.DataFrame): The DataFrame containing the column with missing values.
            column (str): The name of the column to impute missing values.

        Returns:
            pandas.DataFrame: The DataFrame with missing values imputed using the median value of the column.
        """
        df[column] = df[column].fillna(df[column].median())
        return df

    @staticmethod
    def impute_constant(df, column, value):
        """
        Imputes missing values in a specific column of a DataFrame with a constant value.

        This method fills missing values in the specified column using a provided constant value.

        Parameters:
            df (pandas.DataFrame): The DataFrame containing the column with missing values.
            column (str): The name of the column to impute.
            value: The constant value to fill the missing values with.

        Returns:
            pandas.DataFrame: The DataFrame with the missing values imputed.
        """
        df[column] = df[column].fillna(value)
        return df

    @staticmethod
    def delete_missing(df, column):
        """
        Deletes rows with missing values in the specified column.

        This method removes all rows from the DataFrame that contain missing values in the specified column.

        Parameters:
        - df (pandas.DataFrame): The input DataFrame.
        - column (str): The name of the column to check for missing values.

        Returns:
        - pandas.DataFrame: The DataFrame with rows containing missing values in the specified column removed.
        """
        return df.dropna(subset=[column])
