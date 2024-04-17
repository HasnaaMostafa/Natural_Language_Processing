import nltk
from nltk.tokenize import word_tokenize

def pos_tagging(text, tagset):
    tokens = word_tokenize(text)
    if tagset == "universal":
        tagged = nltk.pos_tag(tokens, tagset="universal")
    elif tagset == "treebank":
        tagged = nltk.pos_tag(tokens, tagset="treebank")
    else:
        raise ValueError("Unsupported tagset. Please choose either 'universal' or 'treebank'.")
    return tagged

if __name__ == "__main__":
    text = input("Enter text: ")
    
    try:
        universal_tags = pos_tagging(text, "universal")
        print("\nPart-of-speech tagging using Universal tagset:")
        for word, tag in universal_tags:
            print(f"{word}: {tag}")
        
        treebank_tags = pos_tagging(text, "treebank")
        print("\nPart-of-speech tagging using Treebank tagset:")
        for word, tag in treebank_tags:
            print(f"{word}: {tag}")
    
    except ValueError as ve:
        print(ve)
