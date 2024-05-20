class FeatureEngineer:
    @staticmethod
    def create_new_feature(df, column, func):
        """
        Creates a new feature in the given DataFrame by applying the specified function to the specified column.
        
        This method applies a given function to each element of a specified column, creating a new column 
        with the results.

        Args:
            df (pandas.DataFrame): The DataFrame to modify.
            column (str): The name of the column to apply the function to.
            func (callable): The function to apply to the column. This function should take a single 
                             argument and return a single value.

        Returns:
            pandas.DataFrame: The modified DataFrame with the new feature added as a new column. 
                              The new column will be named as '{column}_new'.
        """
        df[f'{column}_new'] = df[column].apply(func)
        return df
