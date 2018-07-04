from pyramda.function.curry import curry


@curry
def drop_last(n, xs):
    return xs[:-n or None]
