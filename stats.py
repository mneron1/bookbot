def count_words(text):
	words = text.split()
	return len(words)

def count_characters(text):
	char_count = {}
	text = text.lower()
	for char in text:
		char_count[char] = char_count.get(char, 0) + 1
	return char_count

def sort_character_counts(char_count):
    """Takes a dictionary of character counts and returns a sorted list of dictionaries."""
    char_list = [{"char": char, "count": count} for char, count in char_count.items() if char.isalpha()]
    char_list.sort(reverse=True, key=lambda d: d["count"])  # Sort by count (descending)
    return char_list