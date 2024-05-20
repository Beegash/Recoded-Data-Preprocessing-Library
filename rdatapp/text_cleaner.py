import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class TextCleaner:
    def __init__(self):
        """
        Initializes an instance of the TextCleaner class.
        
        This method sets up the necessary attributes for the TextCleaner object.
        It initializes the stop words set with the English stopwords and creates
        a WordNetLemmatizer object for lemmatization.
        """
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def clean_text(self, text):
        """
        Cleans the given text by converting it to lowercase, removing punctuation,
        removing stop words, and lemmatizing the words.

        This method performs several text preprocessing steps:
        1. Converts the text to lowercase.
        2. Removes punctuation.
        3. Removes English stop words.
        4. Lemmatizes the words in the text.

        Args:
            text (str): The text to be cleaned.

        Returns:
            str: The cleaned text.
        """
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        text = ' '.join([word for word in text.split() if word not in self.stop_words])
        text = ' '.join([self.lemmatizer.lemmatize(word) for word in text.split()])
        return text
