from stats import get_num_count

book_path = "books/frankenstein.txt"
def main():
    result = get_num_count(get_book_text(book_path))
    print(f"{result} words found in the document") 

def get_book_text(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

main()