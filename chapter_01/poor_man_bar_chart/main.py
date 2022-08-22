import pprint
from collections import defaultdict
from dataclasses import dataclass

from ui.exceptions import ZeroLengthNotAllowedException
from ui.ui import UI


@dataclass
class PoorManBarChart:
    ui: UI
    alphabet: str = "abcdefghijklmnopqrstuvwxyz"
    mapped = defaultdict(list)

    def main(self):
        text = str(input("Input a text to see the Poor Man Bar Chart : \n"))

        if len(text) == 0:
            raise ZeroLengthNotAllowedException

        text = text.lower()

        for character in text:
            if character in self.alphabet:
                self.mapped[character].append(character)

        self.ui.print("You may need to stretch console window if text wrapping occurs.\n")
        self.ui.print("text = ")
        self.ui.print("text")
        pprint.pprint(self.mapped, width=110)
