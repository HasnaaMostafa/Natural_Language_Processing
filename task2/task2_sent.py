import pandas as pd
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import SnowballStemmer

data = pd.read_csv('UserFeedbackData.csv')

feedback = data['content']

# Tokenization
tokenized_feedback = []
for message in feedback:
    sentences = sent_tokenize(str(message))
    tokenized_feedback.append(sentences)

# Stemming
stemmer = SnowballStemmer("english")
stemmed_feedback = []
for sentences in tokenized_feedback:
    stemmed_sentences = []
    for sentence in sentences:
        tokens = word_tokenize(sentence)
        stemmed_tokens = [stemmer.stem(token) for token in tokens]
        stemmed_sentence = ' '.join(stemmed_tokens)
        stemmed_sentences.append(stemmed_sentence)
    stemmed_feedback.append(stemmed_sentences)

# Print the first 5 tokenized and stemmed sentences
count = 0
for sentences in stemmed_feedback:
    for sentence in sentences:
        print(sentence)
        count += 1
        if count >= 5:
            break
    if count >= 5:
        break