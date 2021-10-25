# package exercises.ex4hangman;

from random import choice
import os.path as p


# File handling for Hangman
#
# Used to read file word.txt containing words to guess.
#
# This doesn't represent some concept, it's just pure functionality, like the
# math module, so we just write bare functions
#
#     *** Nothing to do here ***
def get_random_word_from_file(path_list):
    path = p.join(path_list)
    words = read_file(path)
    the_word = choice(words)
    return the_word


def read_file(path):
    # Use with resource to ensure stream is closed
    with open(path, 'rt', encoding='utf-8') as file_reader:
        lines = []
        while (line := file_reader.readline()) != '':
            lines.append(line.strip('\n'))
        return lines
