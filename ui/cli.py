import os
import sys
from typing import Optional, TextIO


class CLI:
    @staticmethod
    def print_break_line():
        print("\n")

    @staticmethod
    def print(message: str):
        print(message, file=sys.stderr)

    @staticmethod
    def clear():
        os.system("clear")
