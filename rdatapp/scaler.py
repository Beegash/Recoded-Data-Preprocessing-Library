from sklearn.preprocessing import MinMaxScaler, StandardScaler

class Scaler:
    @staticmethod
    def min_max_scale(df, column):
        """
        Applies min-max scaling to a specified column in a DataFrame.

        This method scales the values in the specified column to a range between 0 and 1 
        using the Min-Max scaling technique.

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

        This method transforms the values in the specified column to have a mean of 0 and a standard deviation of 1 
        using the standard scaling technique.

        Parameters:
        - df (pandas.DataFrame): The DataFrame containing the data.
        - column (str): The name of the column to be standardized.

        Returns:
        - df (pandas.DataFrame): The DataFrame with the standardized values in the specified column.
        """
        scaler = StandardScaler()
        df[column] = scaler.fit_transform(df[[column]])
        return df
