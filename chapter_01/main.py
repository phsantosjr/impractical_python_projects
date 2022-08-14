from chapter_01.pig_latin.main import PigLatin
from chapter_01.pseudonyms.main import Pseudonymns
from ui.cli import CLI


def main():
    cli = CLI()
    pseudonyms = Pseudonymns(cli)
    pseudonyms.main()

    pig_latin = PigLatin(cli)
    pig_latin.main()


if __name__ == "__main__":
    main()

