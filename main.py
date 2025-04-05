import sys
from stats import *

def getText(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
    else:
        path = sys.argv[1]
        text = getText(path)
        words = wordCount(text)
        chardict = charCount(text)
        list = dList(chardict)

        def display(path, words, list):
            print(f"============ BOOKBOT ============")
            print(f"Analyzing book found at {path}...")
            print(f"----------- Word Count ----------")
            print(f"Found {words} total words")
            print(f"--------- Character Count -------")
            for each in list:
                print(f"{each['char']}: {each['count']}")

            print(f"============= END ===============")

        display(path, words, list)

main()
    

