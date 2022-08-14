import pytest

from chapter_01.pig_latin.main import PigLatin
from ui.cli import CLI

cli = CLI()


class TestPigLatin:
    def test_vowels_values(self):
        p = PigLatin(ui=cli)
        assert p.vowels == "AEIOU"

    def test_suffix_for_vowel_value(self):
        p = PigLatin(ui=cli)
        assert p.suffix_for_vowel == "WAY"

    def test_suffix_for_consonant_value(self):
        p = PigLatin(ui=cli)
        assert p.suffix_for_consonant == "AY"
