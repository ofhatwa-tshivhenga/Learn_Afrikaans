import sys
import os
import random

# Add parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from word_pairs import word_pairs  # import dictionary from other file

def play_multiple_choice():
    score = 0
    words = list(word_pairs.items())
    
    print("🎮 Welcome to the Afrikaans Multiple Choice Game!")
    print("Type the number of the correct answer. Type 'quit' to stop.\n")
    
    while True:
        english, correct_afrikaans = random.choice(words)
        
        # Get 3 random wrong options
        wrong_options = random.sample(
            [v for k, v in words if v != correct_afrikaans], 
            3
        )
        
        # Mix correct + wrong answers
        options = wrong_options + [correct_afrikaans]
        random.shuffle(options)
        
        print(f"What is '{english}' in Afrikaans?")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        
        answer = input("Your choice (1-4 or 'quit'): ").strip()
        
        if answer.lower() == "quit":
            break
        
        if answer.isdigit() and 1 <= int(answer) <= 4:
            if options[int(answer) - 1] == correct_afrikaans:
                print("✅ Correct!\n")
                score += 1
            else:
                print(f"❌ Wrong! The correct answer was '{correct_afrikaans}'.\n")
        else:
            print("⚠️ Please enter a valid number.\n")
    
    print(f"Game over! Your final score: {score}")

if __name__ == "__main__":
    play_multiple_choice()