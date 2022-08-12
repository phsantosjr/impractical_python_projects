import pytest

from chapter_01.pseudonyms.main import Pseudonymns


class TestPseudonymns:
    def test_total_number_is_number(self):
        p = Pseudonymns()
        assert isinstance(p.total_names, int)



