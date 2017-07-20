from pyramda.function.curry import curry


@curry
def nth(offset, xs):
    return xs[offset]
