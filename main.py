from stats import get_num_count
from stats import get_char_count
from stats import get_sorted_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]
def main():
    book_text = get_book_text(book_path)
    word_count = get_num_count(book_text)
    char_count = get_char_count(book_text)
    sorted_list = get_sorted_list(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["count"]}")
    print("============= END ===============")

def get_book_text(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

main()