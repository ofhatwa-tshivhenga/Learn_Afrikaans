import random
from pathlib import Path

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.utils import get_color_from_hex


from utils import get_word_pairs


CSV_URL = ( "https://docs.google.com/spreadsheets/d/e/2PACX-1vQ5-wdZWc_8Jga7fJKJb2BV0ayl403qss3hsK8xbYXcHBy7U-prB5LLwM6UTfCWwI8TEAhnJDvQ6rRO/pub?output=csv")


class FlashcardGame(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=16, spacing=12, **kwargs)

        # Theme-ish colors
        self.bg = get_color_from_hex("#0b132b")
        self.fg = get_color_from_hex("#e0e6f0")
        self.accent = get_color_from_hex("#5bc0be")
        Window.clearcolor = self.bg

        # State
        self.score = 0
        self.attempts = 0
        self.words = list(get_word_pairs(CSV_URL).items()) # [(english, afrikaans)]
        if not self.words:
            raise RuntimeError("No words loaded. Check your CSV URL or network.")
        random.shuffle(self.words)

        self.pool = self.words.copy() # remaining words
        self.current = None

        # UI Elements
        self.header = Label(text="Afrikaans Flashcards", font_size=28, color=self.fg, size_hint_y=None, height=42)
        self.add_widget(self.header)

        self.meta = Label(text="Score: 0 | 0 attempts", font_size=18, color=self.fg, size_hint_y=None, height=28)
        self.add_widget(self.meta)

        self.question = Label(text="Tap Next to begin", font_size=24, color=self.fg)
        self.add_widget(self.question)

        self.answer_input = TextInput(
        hint_text="Type the Afrikaans word",
        multiline=False,
        size_hint_y=None,
        height=52,
        font_size=20,
        )

        self.answer_input.bind(on_text_validate=self.submit_answer)
        self.add_widget(self.answer_input)


        self.feedback = Label(text="", font_size=20, color=self.fg, size_hint_y=None, height=32)
        self.add_widget(self.feedback)

        # Buttons row 1
        row1 = BoxLayout(size_hint_y=None, height=56, spacing=10)
        self.submit_btn = Button(text="Submit")
        self.submit_btn.bind(on_press=self.submit_answer)
        self.reveal_btn = Button(text="Reveal")
        self.reveal_btn.bind(on_press=self.reveal)
        row1.add_widget(self.submit_btn)
        row1.add_widget(self.reveal_btn)
        self.add_widget(row1)

        # Buttons row 2
        row2 = BoxLayout(size_hint_y=None, height=56, spacing=10)
        self.next_btn = Button(text="Next")
        self.next_btn.bind(on_press=self.next_word)
        self.reset_btn = Button(text="Reset")
        self.reset_btn.bind(on_press=self.reset_game)
        row2.add_widget(self.next_btn)
        row2.add_widget(self.reset_btn)
        self.add_widget(row2)

        # Spacer
        self.add_widget(Widget())


        # Start
        self.next_word()

    def _normalize(self, s: str) -> str:
        """
        Normalize input for comparison.
        You can modify this to always show lowercase/uppercase,
        handle accents, or allow multiword answers.
        """
        return (s or "").strip().lower()
    
    def _update_meta(self):
        remaining = len(self.pool)
        total = len(self.words)
        self.meta.text = f"Score: {self.score} | {self.attempts} attempts | {remaining}/{total} left"

    def next_word(self, *args):
        if not self.pool:
            # Reset the pool but keep score
            self.pool = self.words.copy()
            random.shuffle(self.pool)
        self.current = random.choice(self.pool)
        self.question.text = f"What is '[b]{self.current[0]}[/b]' in Afrikaans?"
        self.question.markup = True
        self.feedback.text = ""
        self.answer_input.text = ""
        self.answer_input.focus = True
        self._update_meta()

    def submit_answer(self, *args):
        if not self.current:
            return
        self.attempts += 1
        english, afrikaans = self.current
        user = self._normalize(self.answer_input.text)
        if user == self._normalize(afrikaans):
            self.score += 1
            self.feedback.text = "✅ Correct!"
            # remove to prevent repeat
            if self.current in self.pool:
                self.pool.remove(self.current)
            self.words.remove(self.current) # More aggressive: remove from total words
            self.current = None
        else:
            self.feedback.text = f"❌ Oops! Correct: [i]{afrikaans}[/i]"
            self.feedback.markup = True
        self._update_meta()

    def reveal(self, *args):
        if self.current:
            self.feedback.text = f"💡 {self.current[1]}"

    def reset_game(self, *args):
        self.score = 0
        self.attempts = 0
        self.words = list(get_word_pairs(CSV_URL).items())
        random.shuffle(self.words)
        self.pool = self.words.copy()
        self.current = None
        self.feedback.text = ""
        self.question.text = "Tap Next to begin"
        self.answer_input.text = ""
        self._update_meta()

class FlashcardApp(App):
       def build(self):
            self.title = "Afrikaans Flashcards"
            return FlashcardGame()



if __name__ == "__main__":
    FlashcardApp().run()