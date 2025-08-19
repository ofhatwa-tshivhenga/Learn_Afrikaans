import sys, os, random, time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import get_word_pairs

CSV_URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ5-wdZWc_8Jga7fJKJb2BV0ayl403qss3hsK8xbYXcHBy7U-prB5LLwM6UTfCWwI8TEAhnJDvQ6rRO/pub?output=csv"
word_pairs = get_word_pairs(CSV_URL)

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
            print(f"✅ Correct! (⏱️    {time_taken} seconds)\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is '{afrikaans}'.\n")
    
    print(f"Game over! Your final score: {score}")

if __name__ == "__main__":
    play_typing_challenge()