from typing import Protocol, Optional, TextIO


class UI(Protocol):
    def print_break_line(self):
        raise NotImplementedError

    def print(self, message: str):
        raise NotImplementedError()

    def clear(self):
        raise NotImplementedError()
