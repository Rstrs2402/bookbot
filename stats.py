def get_book_words(contents):
    words = contents.split()
    return words

def count_book_characters(contents):
    dict_letter_count = {}
    for char in contents:
        char = char.lower()
        if char in dict_letter_count:
            dict_letter_count[char] += 1
        else:
            dict_letter_count[char] = 1
    return dict_letter_count

def sorted_letter_count(letter_count):
    new_dict = [{"char": char, "num": num} for char, num in letter_count.items()]
    new_dict.sort(key=lambda x: x["num"], reverse=True)
    return new_dict
    