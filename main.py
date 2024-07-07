def main():
    book_path = "books/frankenstein.txt"
    print(f"Trying to read from: {book_path}")
    text = get_book_text(book_path)
    print(f"Text length: {len(text)} characters")
    print(text)

def get_book_text(path):
    with open(path) as f:
        print("File opened successfully")
        return f.read()

main()