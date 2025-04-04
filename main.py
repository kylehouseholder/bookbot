from stats import wordCount

def getText(path):
    with open(path) as f:
        return f.read()
    


def main():
    path = "books/frankenstein.txt"
    text = getText(path)
    count = wordCount(text)
    print(f"{count} words found in the document")

main()
    

