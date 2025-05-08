def get_book_text(path):
        with open(path) as f:
                file_contents = f.read()
        return file_contents

def get_num_words(path):
	contents = get_book_text(path)
	num_words = len(contents.split())
	return num_words

def get_num_of_chars(path):
	contents = get_book_text(path)
	chars = {}
	for i in range(len(contents)):
		character = contents[i].lower()
		if character in chars:
			chars[character] += 1
		else:
			chars[character] = 1
	return chars

def sort_on(dict):
	return dict["num"]

def sort_dict(dict):
	new_dict = []
	for key in dict:
		num = dict[key]
		new_key = {
			"char": key,
			"num": num
		}
		new_dict.append(new_key)

	new_dict.sort(reverse=True, key=sort_on)
	return new_dict
