from pyramda.function.curry import curry
from builtins import filter as uncurried_filter


@curry
def filter(p, xs):
    return list(uncurried_filter(p, xs))
