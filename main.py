from stats import *

def getText(path):
    with open(path) as f:
        return f.read()

def main():
    path = "books/frankenstein.txt"
    text = getText(path)
    words = wordCount(text)
    charD = charCount(text)
    dListOut = dList(charD)

    display(path, words, dListOut)

main()
    

