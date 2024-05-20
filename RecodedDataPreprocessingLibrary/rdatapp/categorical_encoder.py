import pandas as pd

from sklearn.preprocessing import OneHotEncoder, LabelEncoder

class CategoricalEncoder:
    @staticmethod
    def one_hot_encode(df, column):
        """
        One-hot encodes a categorical column in a DataFrame.

        Parameters:
        df (pandas.DataFrame): The DataFrame containing the categorical column.
        column (str): The name of the categorical column to be one-hot encoded.

        Returns:
        pandas.DataFrame: The DataFrame with the categorical column one-hot encoded and the original column dropped.
        """
        encoder = OneHotEncoder(sparse_output=False)
        encoded = encoder.fit_transform(df[[column]])
        encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out([column]))
        return pd.concat([df, encoded_df], axis=1).drop(columns=[column])

    @staticmethod
    def label_encode(df, column):
        """
        Encodes the specified column in the given DataFrame using label encoding.

        Parameters:
        - df (pandas.DataFrame): The DataFrame containing the column to be encoded.
        - column (str): The name of the column to be encoded.

        Returns:
        - df (pandas.DataFrame): The DataFrame with the encoded column.
        """
        encoder = LabelEncoder()
        df[column] = encoder.fit_transform(df[column])
        return df
    
    