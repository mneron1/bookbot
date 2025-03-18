import sys
from stats import count_words, count_characters, sort_character_counts

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

# Get the book path from command-line arguments
book_path = sys.argv[1]

try:
    # Load book text
    with open(book_path, "r", encoding="utf-8") as f:
        book_text = f.read()
except FileNotFoundError:
    print(f"Error: The file '{book_path}' was not found.")
    sys.exit(1)
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    sys.exit(1)

# Analyze text
word_count = count_words(book_text)  # Count words
character_counts = count_characters(book_text)  # Get character counts
sorted_characters = sort_character_counts(character_counts)  # Sort characters

# Print report
print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
print(f"Found {word_count} total words")
print("--------- Character Count -------")

for entry in sorted_characters:
    print(f"{entry['char']}: {entry['count']}")

print("============= END ===============")
