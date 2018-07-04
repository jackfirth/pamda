from .adjust import adjust
from pyramda.private.asserts import assert_iterables_equal


def add_one(x):
    return x + 1


def cons_nocurry_test():
    assert_iterables_equal(adjust(add_one, 1, [2, 3]), [2, 4])


def cons_curry_test():
    assert_iterables_equal(adjust(add_one, 1)([2, 3]), [2, 4])
