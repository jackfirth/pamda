from pyramda.function.curry import curry
from .reduce import reduce


@curry
def join(sep, xs):
    return reduce(lambda x, y: x + sep + y, "", xs)
