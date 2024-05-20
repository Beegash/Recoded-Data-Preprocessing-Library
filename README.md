# RDATAPP: Recoded Data Preprocessing Library

[![PyPI version](https://badge.fury.io/py/rdatapp.svg)](https://badge.fury.io/py/rdatapp)
[![Python versions](https://img.shields.io/pypi/pyversions/rdatapp.svg)](https://pypi.python.org/pypi/rdatapp)
[![License](https://img.shields.io/pypi/l/rdatapp.svg)](https://pypi.python.org/pypi/rdatapp)

## Overview

RDATAPP is a comprehensive data preprocessing library designed to handle various data cleaning and transformation tasks. This library includes classes and methods for text cleaning, missing value imputation, one-hot encoding, outlier detection, feature engineering, and more.

## Features

- **Text Cleaning**: Convert text to lowercase, remove punctuation and stopwords, and lemmatize words.
- **Missing Value Handling**: Impute missing values using mean, median, or a constant value. Alternatively, delete rows with missing values.
- **Encoding**: One-hot encode and label encode categorical columns.
- **Outlier Detection**: Detect and remove outliers using the Interquartile Range (IQR) method.
- **Scaling**: Apply Min-Max scaling and standard scaling to numerical columns.
- **Feature Engineering**: Create new features by applying functions to existing columns.
- **Date-Time Handling**: Convert columns to datetime format and extract date parts like year, month, and day.

## Installation

You can install RDATAPP from PyPI using pip:

```sh

pip install rdatapp

```
## Usage

Below are examples of how to use the different classes and methods provided by RDATAPP.

### Text Cleaning

```python
from rdatapp.text_cleaning import TextCleaner

text_cleaner = TextCleaner()
cleaned_text = text_cleaner.clean_text("This is a Sample TEXT, with Punctuation!")
print(cleaned_text)
```

### Missing Value Handling

```python
import pandas as pd
from rdatapp.missing_value_handler import MissingValueHandler

df = pd.DataFrame({'A': [1, 2, None, 4]})
df = MissingValueHandler.impute_mean(df, 'A')
print(df)
```

### Encoding

```python
import pandas as pd
from rdatapp.categorical_encoder import CategoricalEncoder

df = pd.DataFrame({'Category': ['A', 'B', 'A', 'C']})
df = CategoricalEncoder.one_hot_encode(df, 'Category')
print(df)
```

### Outlier Detection

```python
import pandas as pd
from rdatapp.outlier_handler import OutlierHandler

df = pd.DataFrame({'Values': [1, 2, 3, 4, 100]})
df = OutlierHandler.iqr_outlier_detection(df, 'Values')
print(df)
```

### Scaling

```python
import pandas as pd
from rdatapp.scaler import Scaler

df = pd.DataFrame({'Values': [1, 2, 3, 4, 5]})
df = Scaler.min_max_scale(df, 'Values')
print(df)
```

### Feature Engineering

```python
import pandas as pd
from rdatapp.feature_engineer import FeatureEngineer

df = pd.DataFrame({'Values': [1, 2, 3, 4, 5]})
df = FeatureEngineer.create_new_feature(df, 'Values', lambda x: x**2)
print(df)
```

### Date-Time Handling

```python
import pandas as pd
from rdatapp.date_time_handler import DateTimeHandler

df = pd.DataFrame({'Date': ['2021-01-01', '2021-02-01', '2021-03-01']})
df = DateTimeHandler.to_datetime(df, 'Date')
df = DateTimeHandler.extract_date_parts(df, 'Date')
print(df)
```

## Authors

- **Izzettin Furkan Özmen** - [izzettinfurkan.ozmen@stu.fsm.edu.tr](mailto:izzettinfurkan.ozmen@stu.fsm.edu.tr) [linkedin](https://www.linkedin.com/in/izzettinozmen/)
- **Ismail Cifci** - [ismail.cifci@stu.fsm.edu.tr](mailto:ismail.cifci@stu.fsm.edu.tr) [linkedin](https://www.linkedin.com/in/ismail-cifci/)

## License

This project is not licensed. Feel free to use.

## Contributing

We welcome contributions! Please contact us via E-mail addresses.

## Acknowledgments

Special thanks to the instructors who provided guidance and support throughout the development of this project.

## Project Links

- [Source](https://github.com/Beegash/Recoded-Data-Processing-Library)

---

For any issues, please contact the authors or open an issue on GitHub.
