"""Word Finder: finds random words from a dictionary."""


#class WordFinder:

import random

class WordFinder:
    def __init__(self, file_path):
        self.words = []
        self.read_words(file_path)

    def read_words(self, file_path):
        try:
            with open(file_path, 'r') as file:
                self.words = file.read().splitlines()
                print(f"{len(self.words)} words read")
        except FileNotFoundError:
            print("File not found.")

    def random(self):
        return random.choice(self.words)


file_path = 'words.txt'  
random_word = WordFinder(file_path)


word = random_word.random()
if word:
    print("Random word:", word)
