from pyramda.function.curry import curry
from pyramda.iterable.filter import filter


reject = curry(lambda predicate, filterable: filter(
    lambda x: not predicate(x), filterable))
