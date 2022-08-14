from dataclasses import dataclass

from ui.exceptions import ZeroLengthNotAllowedException
from ui.ui import UI


@dataclass
class PigLatin:
    ui: UI
    vowels: str = "AEIOU"
    suffix_for_vowel: str = "WAY"
    suffix_for_consonant: str = "AY"

    def main(self):
        text = str(input("Input a word to see the PigLatin : \n"))

        if len(text) == 0:
            raise ZeroLengthNotAllowedException

        text = text.upper()
        if text[0] in self.vowels:
            text += self.suffix_for_vowel

        else:
            first_letter = text[0]
            text = f"{text[1:]}{first_letter}{self.suffix_for_consonant}"

        self.ui.print(text)
