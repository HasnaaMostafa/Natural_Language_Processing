import spacy

def pos_tagging(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    ud_tags = [(token.text, token.pos_) for token in doc]

    ptb_tags = [(token.text, token.tag_) for token in doc]

    return ud_tags, ptb_tags

if __name__ == "__main__":
    text = input("Enter the text: ")
    ud_tags, ptb_tags = pos_tagging(text)

    print("POS tags with Universal Dependencies tagset:")
    for word, tag in ud_tags:
        print(f"{word}: {tag}")

    print("\nPOS tags with Penn Treebank tagset:")
    for word, tag in ptb_tags:
        print(f"{word}: {tag}")