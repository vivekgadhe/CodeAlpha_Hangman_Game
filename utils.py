# utils.py

def display_word(guessed_word):
    """Return the current state of the guessed word as a string."""
    return " ".join(guessed_word)

def update_word(word, guessed_word, guess):
    """Update guessed_word list if guess is in word."""
    for i, letter in enumerate(word):
        if letter == guess:
            guessed_word[i] = guess
    return guessed_word

def is_valid_guess(guess, guessed_letters):
    """Check if guess is a single alphabet and not already guessed."""
    if len(guess) != 1 or not guess.isalpha():
        return False, "Please enter a single alphabet letter."
    if guess in guessed_letters:
        return False, "You already guessed that letter."
    return True, ""
