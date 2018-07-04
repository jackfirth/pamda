from .juxt import juxt
from pyramda.private.asserts import assert_equal


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def juxt_nocurry_test():
    assert_equal(juxt([add, sub])(1, 2), [3, -1])
