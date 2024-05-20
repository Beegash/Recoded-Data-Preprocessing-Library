from setuptools import setup, find_packages

setup(
    name='rdatapp',
    version='0.5',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scikit-learn',
        'nltk',
    ],
    description='A recoded data preprocessing library for handling various data cleaning and transformation tasks. The library includes classes for text cleaning, missing value imputation, one-hot encoding and more.',
    author='izzettin furkan özmen, ismail cifci',
    author_email='izzettinfurkan.ozmen@stu.fsm.edu.tr, ismail.cifci@stu.fsm.edu.tr',
    url='https://github.com/Beegash/Recoded-Data-Processing-Library',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
