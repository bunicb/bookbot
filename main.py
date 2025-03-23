book_path = "books/frankenstein.txt"
def main():
    result = split_words(get_book_text(book_path))
    print(f"{result} words found in the document") 

def get_book_text(path):
    file_contents = ""
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def split_words(text):
    count = 0
    for word in text.split():
        count += 1
    return count

main()