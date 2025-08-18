import sys
import os
import random

# Add parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from word_pairs import word_pairs  # import dictionary from other file

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