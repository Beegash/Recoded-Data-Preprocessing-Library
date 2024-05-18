import data_preprocessing_lib.__init__ as dpl
import pandas as pd

df = pd.DataFrame({'A': [1, 2, None, 4, 5]})
print(df)
dpl.MissingValueHandler.impute_mean(df, 'A')
print(df)

if __name__ == '__main__':
    import unittest
    unittest.main()
import pandas as pd
from data_preprocessing_lib.categorical_encoder import CategoricalEncoder
from data_preprocessing_lib.data_type_converter import DataTypeConverter
from data_preprocessing_lib.datetime_handler import DateTimeHandler
from data_preprocessing_lib.feature_engineer import FeatureEngineer
from data_preprocessing_lib.outlier_handler import OutlierHandler
from data_preprocessing_lib.scaler import Scaler
from data_preprocessing_lib.text_cleaner import TextCleaner

class TestDataPreprocessing(unittest.TestCase):
    def setUp(self):
        # Set up any necessary data or objects for your tests
        pass

    def tearDown(self):
        # Clean up any resources used by your tests
        pass

    def test_categorical_encoder(self):
        # Test cases for CategoricalEncoder functions
        encoder = CategoricalEncoder()
        df = pd.DataFrame({'A': ['apple', 'banana', 'apple', 'orange', 'banana']})
        encoded_df = encoder.encode(df, 'A')
        self.assertEqual(encoded_df['A_encoded'].tolist(), [0, 1, 0, 2, 1])

    def test_data_type_converter(self):
        # Test cases for DataTypeConverter functions
        converter = DataTypeConverter()
        df = pd.DataFrame({'A': [1, 2, 3], 'B': ['apple', 'banana', 'orange']})
        converted_df = converter.convert(df, {'A': 'str', 'B': 'int'})
        self.assertEqual(converted_df['A'].tolist(), ['1', '2', '3'])
        self.assertEqual(converted_df['B'].tolist(), [0, 1, 2])

    def test_datetime_handler(self):
        # Test cases for DateTimeHandler functions
        handler = DateTimeHandler()
        df = pd.DataFrame({'A': ['2022-01-01', '2022-02-01', '2022-03-01']})
        df['A'] = pd.to_datetime(df['A'])
        df = handler.extract_date_features(df, 'A')
        self.assertEqual(df['A_year'].tolist(), [2022, 2022, 2022])
        self.assertEqual(df['A_month'].tolist(), [1, 2, 3])
        self.assertEqual(df['A_day'].tolist(), [1, 1, 1])

    def test_feature_engineer(self):
        # Test cases for FeatureEngineer functions
        engineer = FeatureEngineer()
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        engineered_df = engineer.create_interaction_features(df, ['A', 'B'])
        self.assertEqual(engineered_df['A*B'].tolist(), [4, 10, 18])

    def test_outlier_handler(self):
        # Test cases for OutlierHandler functions
        handler = OutlierHandler()
        df = pd.DataFrame({'A': [1, 2, 3, 100]})
        df = handler.remove_outliers(df, 'A')
        self.assertEqual(df['A'].tolist(), [1, 2, 3])

    def test_scaler(self):
        # Test cases for Scaler functions
        scaler = Scaler()
        df = pd.DataFrame({'A': [1, 2, 3]})
        scaled_df = scaler.scale(df, 'A')
        self.assertAlmostEqual(scaled_df['A'].tolist(), [-1.22474487, 0, 1.22474487], places=5)

    def test_text_cleaner(self):
        # Test cases for TextCleaner functions
        cleaner = TextCleaner()
        df = pd.DataFrame({'A': ['apple!', 'banana?', 'orange.']})
        cleaned_df = cleaner.clean_text(df, 'A')
        self.assertEqual(cleaned_df['A'].tolist(), ['apple', 'banana', 'orange'])

if __name__ == '__main__':
    unittest.main()