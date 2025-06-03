from stats import get_book_words, count_book_characters, sorted_letter_count
import sys


def get_books_text(file_path):
    contents = ""
    with open(file_path) as file:
        contents = file.read()
    return contents
  
def main(filename):
    if len (sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filename = sys.argv[1]
        book_text = get_books_text(filename)
        num_words = len(get_book_words(book_text))
        char_count = count_book_characters(book_text)
        sorted_char = sorted_letter_count(char_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filename}")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for char in sorted_char:
            if char['char'].isalpha():
                print(f"{char['char']}: {char['num']}")

        print("============= END ===============")
    
    
main("")