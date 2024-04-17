import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

languages = ['english', 'spanish', 'french', 'german', 'italian']
for lang in languages:
    print(f"Stop words in {lang}:")
    print(stopwords.words(lang))
    print()
