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