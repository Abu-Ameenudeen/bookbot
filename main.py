def main():
    path_to_file = r"books/frankenstein.txt"
    text = read_text(path_to_file)
    print(count_words(text))


def count_words(sting):
    list_of_words = sting.split()
    return len(list_of_words)


def read_text(book_path):
    with open(book_path) as infile:
        file_contents = infile.read()
        return file_contents

main()
