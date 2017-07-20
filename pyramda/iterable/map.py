from pyramda.function.curry import curry


@curry
def map(f, xs):
    if callable(getattr(xs, 'map', None)):
        return xs.map(f)
    return [f(x) for x in xs]
