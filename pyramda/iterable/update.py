from pyramda.function.curry import curry

"""This functions applies function at given index"""
update = curry(lambda i, v, xs: [
               v if i == ind else x for ind, x in enumerate(xs)])
