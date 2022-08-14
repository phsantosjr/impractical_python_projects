import pytest

from chapter_01.pseudonyms.main import Pseudonymns
from ui.cli import CLI

cli = CLI()


class TestPseudonymns:
    def test_total_number_is_number(self):
        p = Pseudonymns(cli)
        assert isinstance(p.total_names, int)

