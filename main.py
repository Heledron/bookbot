from stats import get_num_words, get_chars_dict, sort_chars
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_list = sort_chars(chars_dict)
    print(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...") 
    print("----------- Word Count ----------")  
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")   
    for item in chars_list:
        ch = item["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {item['num']}")

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
