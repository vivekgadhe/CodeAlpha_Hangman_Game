
import random
from words import words_list
from utils import display_word, update_word, is_valid_guess

def hangman():
    word = random.choice(words_list)
    guessed_word = ["_"] * len(word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")
    print("Guess the word:", display_word(guessed_word))

    while attempts > 0 and "_" in guessed_word:
        guess = input("Enter a letter: ").lower()

        valid, message = is_valid_guess(guess, guessed_letters)
        if not valid:
            print(message)
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
            guessed_word = update_word(word, guessed_word, guess)
        else:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")

        print("Word:", display_word(guessed_word))

    if "_" not in guessed_word:
        print("🎉 Congratulations! You guessed the word:", word)
    else:
        print("❌ Game over! The word was:", word)

if __name__ == "__main__":
    hangman()
