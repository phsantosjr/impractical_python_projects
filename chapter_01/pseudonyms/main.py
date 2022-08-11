import sys
import random
from dataclasses import dataclass, field
from faker import Faker

from ui.exceptions import ZeroOrLessNotAllowedException


@dataclass
class Pseudonymns:
    first_names: list = field(default_factory=list)
    middle_names: list = field(default_factory=list)
    last_names: list = field(default_factory=list)
    total_names: int = 100
    language: str = "PT-BR"
    fake: any = None

    def __post_init__(self):
        if self.total_names <= 0:
            raise ZeroOrLessNotAllowedException

        self.fake = Faker(self.language)
        self._load_first_names()
        self._load_middle_names()
        self._load_last_names()

    def _load_first_names(self):
        self.first_names = [self.fake.first_name_nonbinary() for _ in range(self.total_names)]

    def _load_middle_names(self):
        self.middle_names = [self.fake.last_name_nonbinary() for _ in range(self.total_names)]

    def _load_last_names(self):
        self.last_names = [self.fake.last_name_nonbinary() for _ in range(self.total_names)]

    def get_first_name(self) -> str:
        return random.choice(self.first_names)

    def get_middle_name(self) -> str:
        return random.choice(self.middle_names)

    def get_last_name(self) -> str:
        return random.choice(self.last_names)


def main():
    pseudonyms = Pseudonymns()

    while True:
        first_name = pseudonyms.get_first_name()
        middle_name = pseudonyms.get_middle_name()
        last_name = pseudonyms.get_last_name()

        print("\n\n")
        print(f"The name has been chosen was {first_name} {middle_name} {last_name}", file=sys.stderr)
        print("\n\n")
        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")


if __name__ == "__main__":
    main()
