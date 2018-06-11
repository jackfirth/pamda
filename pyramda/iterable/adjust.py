from pyramda.function.curry import curry

"""This functions applies function at given index"""
adjust = curry(lambda f, i, xs: [f(x) if i == ind else x for ind, x in enumerate(xs)])
