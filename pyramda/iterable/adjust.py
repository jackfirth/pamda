from pyramda.function.curry import curry


@curry
def adjust(f, i, xs):
    return [f(x) if i == ind else x for ind, x in enumerate(xs)]
