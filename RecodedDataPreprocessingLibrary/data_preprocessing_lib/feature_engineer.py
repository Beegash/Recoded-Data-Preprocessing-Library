class FeatureEngineer:
    @staticmethod
    def create_new_feature(df, column, func):
        """
        Creates a new feature in the given DataFrame by applying the specified function to the specified column.

        Args:
            df (pandas.DataFrame): The DataFrame to modify.
            column (str): The name of the column to apply the function to.
            func (callable): The function to apply to the column.

        Returns:
            pandas.DataFrame: The modified DataFrame with the new feature added.
        """
        df[f'{column}_new'] = df[column].apply(func)
        return df