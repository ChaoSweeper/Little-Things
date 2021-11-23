import os


# run main program
def main():
    filename = locate_file("specs.txt")
    lines, words, characters, unique_words, special_characters = load_text(filename)
    display_stats(lines, words, characters, unique_words, special_characters)


# search for the file in the current directory
# if not found, search for the file in the parent directory


def locate_file(filename):
    if os.path.exists(filename):
        return filename
    else:
        return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)


# load text file and return a list of lines, list of words, and list of characters,
# list of unique words, and list of special characters
def load_text(filename):
    with open(filename, "r") as f:
        text = f.read()
    lines = text.split("\n")
    words = text.split()
    characters = list(text)
    unique_words = list(set(words))
    special_characters = list(set(characters))
    return lines, words, characters, unique_words, special_characters


# display the number of lines, words, characters, unique words, and special characters
def display_stats(lines, words, characters, unique_words, special_characters):
    print("Number of lines:", len(lines))
    print("Number of words:", len(words))
    print("Number of characters:", len(characters))
    print("Number of unique words:", len(unique_words))
    print("Number of special characters:", len(special_characters))


# initialize program
if __name__ == "__main__":
    main()
