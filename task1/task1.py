from nltk.tokenize import word_tokenize, sent_tokenize

def tokenize_words(text):
    words = word_tokenize(text)
    return words

def tokenize_sentences(text):
    sentences = sent_tokenize(text)
    return sentences

def split_text(text):
    return text.split()

def main():
    text = input("Enter the text: ")
    choice = int(input("Choose one of the following options:\n1. Print tokenized words\n2. Print tokenized sentences\n3. Print output using split function\n"))

    if choice == 1:
        tokenized_words = tokenize_words(text)
        print("Tokenized words:", tokenized_words)
    elif choice == 2:
        tokenized_sentences = tokenize_sentences(text)
        print("Tokenized sentences:", tokenized_sentences)
    elif choice == 3:
        split_output = split_text(text)
        print("Output using split function:", split_output)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
