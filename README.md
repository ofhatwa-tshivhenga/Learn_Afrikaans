# Learn Afrikaans – CLI Games

A small suite of console games (Flashcards, Hangman, Multiple Choice, Typing) that use English↔Afrikaans word pairs.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cd Learn_Afrikaans

python3 Hangmangame/game.py
# or:
python3 flashboardgame/game.py
python3 multiple_choice/game.py
python3 typing_game/game.py
