from pyramda.function.curry import curry
from builtins import range as arange


@curry
def range(start, end):
    return arange(start, end)
