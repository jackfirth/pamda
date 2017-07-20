from pyramda.function.curry import curry
from pyramda.iterable.filter import filter


@curry
def reject(predicate, filterable):
    return filter(lambda x: not predicate(x), filterable)
