def wordCount(text):
    list = text.split()
    return len(list)

def charCount(text):
    ltext = text[::1].lower()
    counts = {}
    for char in ltext:   
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def whichval(input):
    return input["count"]
    
def dList(input):
    out = []    # list'o'dicts
    for char, count in input.items():
        if char.isalpha():
            entry = {
                "char": char,
                "count": count
            }
            out.append(entry)
    out.sort(key=whichval, reverse=True)
    return out

