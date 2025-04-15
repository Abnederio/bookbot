import sys
from stats import word_count, char_count, sort_count

def main():
   
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    
    text = get_book_text(book_path)
    
    word_counts = word_count(text)
    print(f"Found {word_counts} total words")

    print(sort_count(char_count(text)))

def get_book_text(path):
    try:
        with open(path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()

