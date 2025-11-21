
def get_book_text(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
        return file_contents

def char_count(string):
    char_array = list(string)
    char_dict = {}
    for char in char_array:
        char = char.lower()
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(items):
    return items["num"]

def sort_dictionary(d):
    sorted_dictionaries = []
    for key in d:
        dictionary = {"char": key, "num": d[key]}
        sorted_dictionaries.append(dictionary)
    sorted_dictionaries.sort(reverse=True, key=sort_on)
    return sorted_dictionaries
