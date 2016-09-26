from pyramda.function.curry import curry


reject = curry(lambda predicate, filterable: filter(lambda x: not predicate(x), filterable))
