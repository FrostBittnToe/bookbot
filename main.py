import sys
from stats import get_num_words
from stats import character_frequency
from stats import sort_character_counts

def get_book_text(filepath):
    with open(filepath, 'r') as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <books>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    num_words = get_num_words(book_text)
    char_count = character_frequency(book_text)
    sorted_char_counts = sort_character_counts(char_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_char_counts:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

main()