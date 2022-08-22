import pytest

from chapter_01.poor_man_bar_chart.main import PoorManBarChart
from ui.cli import CLI
from ui.exceptions import ZeroLengthNotAllowedException

cli = CLI()


class TestPoorManBarChart:
    def test_alphabet_values(self):
        p = PoorManBarChart(ui=cli)
        assert p.alphabet == "abcdefghijklmnopqrstuvwxyz"

    def test_raise_empty_error(self, monkeypatch):
        with pytest.raises(ZeroLengthNotAllowedException):
            monkeypatch.setattr('builtins.input', lambda _: "")
            p = PoorManBarChart(ui=cli)
            p.main()

