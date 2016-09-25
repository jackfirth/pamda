from pyramda.function.curry import curry


@curry
def nth(offset, xs):
    idx = offset + len(xs) if offset < 0 else offset
    return xs[idx]
