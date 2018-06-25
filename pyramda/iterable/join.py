from pyramda.function.curry import curry

@curry
def join(sep, xs):
    return str(sep).join(xs)
