from stats import get_num_count
from stats import get_char_count

book_path = "books/frankenstein.txt"
def main():
    book_text = get_book_text(book_path)
    word_count = get_num_count(book_text)
    char_count = get_char_count(book_text)
    print(f"{word_count} words found in the document") 
    print(char_count)

def get_book_text(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

main()