from pyramda.function.curry import curry

arange = range

@curry
def range(start, end):
    return xrange(start, end)
