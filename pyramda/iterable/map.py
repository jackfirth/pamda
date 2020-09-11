from pyramda.function.curry import curry
from builtins import map as uncurried_map


@curry
def map(f, xs):
    return list(uncurried_map(f, xs))
