import sys

def main():

	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	from stats import get_num_words
	from stats import get_num_of_chars
	from stats import sort_dict

	book = sys.argv[1]

	num_words = get_num_words(book)
	chars = get_num_of_chars(book)
	dict = sort_dict(chars)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
	for char in dict:
		print(f"{char["char"]}: {char["num"]}")
	print("============= END ===============")

	return

main()
