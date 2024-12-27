def main():
    path_to_file = r"books/frankenstein.txt"
    print(read_text(path_to_file))


def read_text(book_path):
    with open(book_path) as infile:
        file_contents = infile.read()
        return file_contents

main()
