import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import SnowballStemmer

data = pd.read_csv('UserFeedbackData.csv')

feedback = data['content']

# Tokenization
tokenized_feedback = []
for message in feedback:
    sentences = sent_tokenize(str(message))
    tokens = [word_tokenize(sentence) for sentence in sentences]
    tokenized_feedback.append(tokens)

# Stemming
stemmer = SnowballStemmer("english")
stemmed_feedback = []
for sentences in tokenized_feedback:
    stemmed_sentences = []
    for tokens in sentences:
        stemmed_tokens = [stemmer.stem(token) for token in tokens]
        stemmed_sentences.append(stemmed_tokens)
    stemmed_feedback.append(stemmed_sentences)

# Print the tokenized and stemmed feedback
for sentences in stemmed_feedback:
    for tokens in sentences:
        print(tokens)