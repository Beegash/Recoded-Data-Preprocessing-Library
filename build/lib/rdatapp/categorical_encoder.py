import pandas as pd

from sklearn.preprocessing import OneHotEncoder, LabelEncoder

class CategoricalEncoder:
    @staticmethod
    def one_hot_encode(df, column):
        """
        One-hot encodes a categorical column in a DataFrame.
        
        This method converts a categorical column into a new DataFrame with binary columns 
        for each category and then concatenates it to the original DataFrame, dropping the original column.

        Parameters:
        df (pandas.DataFrame): The DataFrame containing the categorical column.
        column (str): The name of the categorical column to be one-hot encoded.

        Returns:
        pandas.DataFrame: The DataFrame with the one-hot encoded column and the original column removed.
        """
        encoder = OneHotEncoder(sparse_output=False)
        encoded = encoder.fit_transform(df[[column]])
        encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out([column]))
        return pd.concat([df, encoded_df], axis=1).drop(columns=[column])

    @staticmethod
    def label_encode(df, column):
        """
        Label encodes a categorical column in a DataFrame.

        This method converts each category in a column into a numeric label. This is useful 
        for converting categorical data into a format suitable for machine learning algorithms 
        that require numerical input.

        Parameters:
        df (pandas.DataFrame): The DataFrame containing the column to be label encoded.
        column (str): The name of the column to be label encoded.

        Returns:
        pandas.DataFrame: The DataFrame with the label encoded column.
        """
        encoder = LabelEncoder()
        df[column] = encoder.fit_transform(df[column])
        return df
    
    