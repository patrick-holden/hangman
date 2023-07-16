import random

class Hangman:
    def __init__(self, word_list, num_lives):
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        self.letters_remaining = list(self.word)
        self.attempted_letters = []

    def ask_for_input(self):
        while self.num_lives>0 and len(self.letters_remaining) > 0:
          try:
            guess = input("Guess a letter: ")
            if len(guess) == 1 and guess.isalpha():
                self.check_guess(guess)
            else:
                print("\nInvalid guess. Please enter a single alphabetical character.\n")
          except KeyboardInterrupt:
            break

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.letters_remaining:
            self.letters_remaining.remove(guess)
            self.attempted_letters.append(guess)
            print(f"Good guess! '{guess}' is in the word.\n")
        elif guess in self.attempted_letters:
            print("\nYou already tried that letter!\n")
        else:
            print(f"Sorry, '{guess}' is not in the word.\n")
            self.num_lives = self.num_lives-1