import sys, os, random
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_word_pairs

CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ5-wdZWc_8Jga7fJKJb2BV0ayl403qss3hsK8xbYXcHBy7U-prB5LLwM6UTfCWwI8TEAhnJDvQ6rRO/pub?output=csv"
word_pairs = get_word_pairs(CSV_URL)

def play_game():
    score = 0
    words = list(word_pairs.items())
    
    print("Welcome to the Afrikaans Flashcard Game!")
    print("Type the Afrikaans translation for each English word.")
    print("Type 'quit' to stop playing.\n")

    while True:
        english, afrikaans = random.choice(words)
        answer = input(f"What is '{english}' in Afrikaans? ").strip().lower()

        if answer == "quit":
            break

        if answer == afrikaans:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Oops! The correct answer is '{afrikaans}'.\n")

    print(f"Game over! Your final score: {score}")

if __name__ == "__main__":
    play_game()