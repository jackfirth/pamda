from pyramda.function.curry import curry


@curry
def map(f, xs):
    if callable(getattr(xs, 'map', None)):
        return xs.map(f)
    if callable(getattr(xs, 'fmap', None)):
        return xs.fmap(f)
    return [f(x) for x in xs]

fmap = map
