# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!")
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
import string


def read_file_content(filename):
    # Opens and reads the contents in the file
    with open(filename) as file:
        file_content = file.read()
        # Returns the contemts of the file
    return file_content


def count_words():
    text = read_file_content("story.txt")
    text = text.translate(str.maketrans("", "", string.punctuation))
    word_count = {}
    split_text = text.split()

    for word in split_text:
            word_count[word] = split_text.count(word)
    return word_count        
        
print(count_words())