def main():
    path_to_file = r"books/frankenstein.txt"
    entire_text = read_text(path_to_file)
    total_words = count_words(entire_text)
    all_characters_dict = count_characters(entire_text)
    char_dict_list = dict_to_list(all_characters_dict)
    char_dict_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{total_words} words found in the document")
    print()
    for item in char_dict_list:
        if item["char"].isalpha():
            print(f"The \'{item['char']}\' character was found {item['times']} times")
    print("--- End report ---")


def sort_on(dict_item):
    return dict_item["times"]


def dict_to_list(char_dict):
    char_list = []
    for item in char_dict:
        char_list.append({
            "char": item, 
            "times": char_dict[item]
            })
    return char_list


def count_words(sting):
    list_of_words = sting.split()
    return len(list_of_words)


def count_characters(text):
    characters_dict = {}
    lower_text_contents = text.lower()
    for letter in lower_text_contents:
        if letter in characters_dict:
            characters_dict[letter] += 1
        else:
            characters_dict[letter] = 1
    return characters_dict


def read_text(book_path):
    with open(book_path) as infile:
        file_contents = infile.read()
        return file_contents


main()
