import time
import sys
import os
import random

# Add parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from word_pairs import word_pairs  # import dictionary from other file

def play_typing_challenge():
    score = 0
    words = list(word_pairs.items())
    
    print("⌨️ Welcome to the Afrikaans Typing Challenge!")
    print("Translate the English word into Afrikaans as fast as you can!")
    print("Type 'quit' to stop playing.\n")
    
    while True:
        english, afrikaans = random.choice(words)
        print(f"Translate: {english}")
        
        start_time = time.time()
        answer = input("Your answer: ").strip().lower()
        end_time = time.time()
        
        if answer == "quit":
            break
        
        if answer == afrikaans:
            time_taken = round(end_time - start_time, 2)
            print(f"✅ Correct! (⏱️ {time_taken} seconds)\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is '{afrikaans}'.\n")
    
    print(f"Game over! Your final score: {score}")

if __name__ == "__main__":
    play_typing_challenge()