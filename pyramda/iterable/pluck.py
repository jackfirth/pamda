from pyramda.function.curry import curry


@curry
def prop(key, x):
    try:
        return x[key]
    except KeyError:
        return None


@curry
def pluck(key, xs):
    return list(map(prop(key), xs))
