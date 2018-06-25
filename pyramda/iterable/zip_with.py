from pyramda.function.curry import curry

"""This functions takes two list and applies given function to it"""
zip_with = curry(lambda f, xs1, xs2: [f(x, y) for x, y in zip(xs1, xs2)])
