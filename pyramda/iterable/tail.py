from pyramda.function.curry import curry


tail = curry(lambda xs: xs[1:])
