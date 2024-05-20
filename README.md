# RDATAPP: Recoded Data Preprocessing Library

[![PyPI version](https://badge.fury.io/py/rdatapp.svg)](https://badge.fury.io/py/rdatapp)
[![Python versions](https://img.shields.io/pypi/pyversions/rdatapp.svg)](https://pypi.python.org/pypi/rdatapp)
[![License](https://img.shields.io/pypi/l/rdatapp.svg)](https://pypi.python.org/pypi/rdatapp)

## Overview

RDATAPP is a comprehensive data preprocessing library designed to handle various data cleaning and transformation tasks. This library includes classes and methods for text cleaning, missing value imputation, one-hot encoding, outlier detection, feature engineering, and more.

## Project Goals and Features
**Goals:**

The primary goal of this project was to develop a comprehensive data preprocessing library, RDATAPP, which facilitates various data cleaning and transformation tasks. The library aims to provide easy-to-use tools for handling common data preprocessing steps such as missing value imputation, text cleaning, one-hot encoding, outlier detection, feature engineering, and scaling.

**Features:**

- **Text Cleaning**: Convert text to lowercase, remove punctuation and stopwords, and lemmatize words.
- **Missing Value Handling**: Impute missing values using mean, median, or a constant value. Alternatively, delete rows with missing values.
- **Encoding**: One-hot encode and label encode categorical columns.
- **Outlier Detection**: Detect and remove outliers using the Interquartile Range (IQR) method.
- **Scaling**: Apply Min-Max scaling and standard scaling to numerical columns.
- **Feature Engineering**: Create new features by applying functions to existing columns.
- **Date-Time Handling**: Convert columns to datetime format and extract date parts like year, month, and day.
- **Design:**
The RDATAPP library was designed to be modular, with each preprocessing task encapsulated within its own class. This approach promotes reusability and makes it easier to maintain and extend the library.

## Implementation:
The library is structured with the following core components:

- **TextCleaner:** Handles text cleaning operations.
- **MissingValueHandler:** Manages missing value imputation.
- **CategoricalEncoder:** Performs one-hot encoding and label encoding.
- **OutlierHandler:** Detects and removes outliers.
- **Scaler:** Scales numerical data using Min-Max or standard scaling.
- **FeatureEngineer:** Creates new features from existing data.
- **DateTimeHandler:** Handles datetime conversion and extraction of date parts.

Each class contains static methods to ensure that the functions can be called without instantiating the class, making the usage straightforward.

## PyPI Packaging:
The project was packaged for PyPI distribution, following these steps:

- **Setup File:** Created a setup.py file to define the package details and dependencies.
- **README File:** Included a README.md file for the long description on the PyPI page.
- **Building the Package:** Used setuptools to build the package.
- **Uploading to PyPI:** Used twine to upload the package to PyPI.
- **Examples of Library Usage with a Dataset
Dataset:**
The dataset used in this example is a CSV file containing movie information with the following columns: Movie_Id, Genre, Release Date, Rating, Summary, Shooting Location, Budget in USD, Awards, and Popular.
- **Evaluation of the Library's Functionality and Performance
Functionality:**
The RDATAPP library successfully provides a comprehensive set of tools for common data preprocessing tasks. The modular design allows users to easily apply individual preprocessing steps without unnecessary complexity. Each component has been tested and demonstrated to work effectively with a sample dataset.

## Performance:
The performance of the library is adequate for typical data preprocessing tasks. The operations are efficient and can handle reasonably large datasets within acceptable time limits. However, performance can be impacted by the size of the dataset and the specific preprocessing tasks being performed.


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

## Notes


## Authors

- **Izzettin Furkan Özmen** - [izzettinfurkan.ozmen@stu.fsm.edu.tr](mailto:izzettinfurkan.ozmen@stu.fsm.edu.tr) [linkedin](https://www.linkedin.com/in/izzettinozmen/)
- **Ismail Cifci** - [ismail.cifci@stu.fsm.edu.tr](mailto:ismail.cifci@stu.fsm.edu.tr) [linkedin](https://www.linkedin.com/in/ismail-cifci/)

## License

This project is not licensed, feel free to use.

## Contributing

We welcome contributions! Please contact us via E-mail addresses.

## Acknowledgments

Special thanks to the instructors who provided guidance and support throughout the development of this project.

## Project Links

- [Source](https://github.com/Beegash/Recoded-Data-Processing-Library)

---

For any issues, please contact the authors or open an issue on GitHub.
