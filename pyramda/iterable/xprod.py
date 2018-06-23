from pyramda.function.curry import curry

"""This functions takes cross product of two list"""


xprod = curry(lambda xs1, xs2: [[x, y] for y in xs2 for x in xs1])
