import pandas as pd

class OutlierHandler:
    @staticmethod
    def iqr_outlier_detection(df, column, threshold=1.5):
        """
        Perform outlier detection using the Interquartile Range (IQR) method.
        
        This method identifies and removes outliers from the specified column in the DataFrame 
        based on the IQR method. Outliers are defined as values below Q1 - (IQR * threshold) 
        or above Q3 + (IQR * threshold), where Q1 and Q3 are the first and third quartiles, respectively.

        Args:
            df (pandas.DataFrame): The input DataFrame.
            column (str): The column name to perform outlier detection on.
            threshold (float, optional): The threshold value to determine outliers. Defaults to 1.5.

        Returns:
            pandas.DataFrame: The filtered DataFrame without outliers.
        """
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - (IQR * threshold)
        upper_bound = Q3 + (IQR * threshold)
        return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
