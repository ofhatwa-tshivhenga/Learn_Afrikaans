import sys, os, random
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_word_pairs

CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ5-wdZWc_8Jga7fJKJb2BV0ayl403qss3hsK8xbYXcHBy7U-prB5LLwM6UTfCWwI8TEAhnJDvQ6rRO/pub?output=csv"
word_pairs = get_word_pairs(CSV_URL)

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def play_hangman():
    afrikaans_word = random.choice(list(word_pairs.values()))
    guessed_letters = set()
    attempts_left = 6
    
    print("🎮 Welcome to Afrikaans Hangman!")
    print("Guess the Afrikaans word, one letter at a time.\n")

    while attempts_left > 0:
        print(f"Word: {display_word(afrikaans_word, guessed_letters)}")
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}\n")

        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter!\n")
            continue

        guessed_letters.add(guess)

        if guess in afrikaans_word:
            print("✅ Correct!\n")
            if all(letter in guessed_letters for letter in afrikaans_word):
                print(f"🎉 Congrats! You guessed the word: {afrikaans_word}")
                return
        else:
            attempts_left -= 1
            print("❌ Wrong guess!\n")

    print(f"💀 Game over! The word was: {afrikaans_word}")

if __name__ == "__main__":
    play_hangman()