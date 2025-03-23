book_path = "books/frankenstein.txt"
def main():
    print(get_book_text(book_path))
    

def get_book_text(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

main()