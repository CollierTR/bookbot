import sys
from stats import get_book_text
from stats import char_count
from stats import sort_dictionary



def print_report(data, total_words, book_name):
    def formatted_char_count():
        for entry in data:
            if entry['char'].isalpha():
                print(f"{entry['char']}: {entry['num']}")
    print(f"""
============ BOOKBOT ============
Analyzing book found at {book_name}...
----------- Word Count ----------
Found {total_words} total words
--------- Character Count -------""")
    formatted_char_count()
    print("============= END ===============")




def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_name = sys.argv[1]    
    book = get_book_text(book_name)
    num_words = book.split()
    individual_char_count = char_count(book)
    individual_char_count = sort_dictionary(individual_char_count)
    print_report(individual_char_count, len(num_words), book_name)



main()
