def main():
    path_to_file = r"books/frankenstein.txt"
    entire_text = read_text(path_to_file)
    total_words = count_words(entire_text)
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{total_words} words found in the document")
    print()


def count_words(sting):
    list_of_words = sting.split()
    return len(list_of_words)


def count_characters(text):
    characters = {}
    for letter in text:
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1
    return characters


def read_text(book_path):
    with open(book_path) as infile:
        file_contents = infile.read()
        return file_contents


main()
