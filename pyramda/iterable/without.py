from pyramda.function.curry import curry

"""Returns a new list without values in the first argument"""

a = [1, 2]
b = [1, 2, 1, 3, 4]

without = curry(lambda xs1, xs2: [x for x in xs2 if x not in xs1])
