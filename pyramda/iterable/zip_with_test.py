from .zip_with import zip_with
from pyramda.private.asserts import assert_iterables_equal


def add(a, b):
    return a + b


def uniq_nocurry_test():
    assert_iterables_equal(zip_with(add, [1, 1, 1], [1, 2, 3]), [2, 3, 4])


def take_curry_test():
    assert_iterables_equal(zip_with(add)([1, 1, 1], [1, 2, 3]), [2, 3, 4])
