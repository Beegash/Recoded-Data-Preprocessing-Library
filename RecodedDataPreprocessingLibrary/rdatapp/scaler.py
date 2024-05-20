from sklearn.preprocessing import MinMaxScaler, StandardScaler

class Scaler:
    @staticmethod
    def min_max_scale(df, column):
        """
        Applies min-max scaling to a specified column in a DataFrame.

        Parameters:
        - df (pandas.DataFrame): The DataFrame to be scaled.
        - column (str): The name of the column to be scaled.

        Returns:
        - df (pandas.DataFrame): The DataFrame with the scaled column.
        """
        scaler = MinMaxScaler()
        df[column] = scaler.fit_transform(df[[column]])
        return df

    @staticmethod
    def standard_scale(df, column):
        """
        Standardizes the values in the specified column of the DataFrame using the StandardScaler.

        Parameters:
        df (pandas.DataFrame): The DataFrame containing the data.
        column (str): The name of the column to be standardized.

        Returns:
        pandas.DataFrame: The DataFrame with the standardized values in the specified column.
        """
        scaler = StandardScaler()
        df[column] = scaler.fit_transform(df[[column]])
        return df