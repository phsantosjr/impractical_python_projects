class ZeroOrLessNotAllowedException(Exception):
    def __str__(self):
        return "You must inform a value greater then 0 (zero)"
