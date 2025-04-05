from stats import *

def getText(path):
    with open(path) as f:
        return f.read()
    


def main():
    path = "books/frankenstein.txt"
    text = getText(path)
    words = wordCount(text)
    chars = charCount(text)
    print(f"{words} words found in the document")
    print(chars)
main()
    

