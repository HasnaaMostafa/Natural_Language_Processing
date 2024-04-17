import spacy

def tokenize_sentences(text, language_code):
    if language_code == "en":
        nlp = spacy.load("en_core_web_sm")
    elif language_code == "fr":
        nlp = spacy.load("fr_core_news_sm")
    elif language_code == "es":
        nlp = spacy.load("es_core_news_sm")
    elif language_code == "de":
        nlp = spacy.load("de_core_news_sm")
    else:
        raise ValueError("Unsupported language code.")
    
    doc = nlp(text)
    sentences = [sent.text for sent in doc.sents]
    return sentences

if __name__ == "__main__":
    text = input("Enter text: ")
    language_code = input("Enter language code (e.g., en for English, fr for French, es for Spanish, de for German): ")
    tokenized_sentences = tokenize_sentences(text, language_code)
    print("Tokenized sentences:")
    for i, sentence in enumerate(tokenized_sentences, start=1):
        print(f"Sentence {i}: {sentence}")

##Bonjour le monde. comment vas-tu ?