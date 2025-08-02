
def count_words(book):
    count = 0
    words = book.split()
    for word in words:
        count +=1
    return count
def count_chars(book):
    
    chars = list(book)
    count = {
        "a": 0
    }
    for char in chars:
        if char.lower() in count:
            count[char.lower()] += 1
        else :
            count[char.lower()] = 1 
    
    return count
def sortDict(dictionary):
    return sorted(dictionary.items(), key=sort_on, reverse=True)

def sort_on(items):
    return items[1]