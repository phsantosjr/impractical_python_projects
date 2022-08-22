from chapter_01.pig_latin.main import PigLatin
from chapter_01.poor_man_bar_chart.main import PoorManBarChart
from chapter_01.pseudonyms.main import Pseudonymns
from ui.cli import CLI


def main():
    cli = CLI()
    pseudonyms = Pseudonymns(cli)
    pseudonyms.main()

    pig_latin = PigLatin(cli)
    pig_latin.main()

    poor_man = PoorManBarChart(cli)
    poor_man.main()


if __name__ == "__main__":
    main()

