from stats import count_words, count_chars, sortDict
import sys
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)



    count = count_words(get_book_text(sys.argv[1]))
    charCount = count_chars(get_book_text(sys.argv[1]))
    sorted = sortDict(charCount)
    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    
    print(f"Found {count} total words")
    
    print("--------- Character Count -------")
    for char, freq in sorted:
        print(f"{char}: {freq}")

def get_book_text(filepath):
    with open(filepath) as f:
        return(f.read())


main()