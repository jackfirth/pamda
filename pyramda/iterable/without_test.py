from pyramda.private.asserts import assert_iterables_equal
from .without import without


def uniq_nocurry_test():
    assert_iterables_equal(without([1, 2], [1, 2, 1, 3, 4]), [3, 4])


def take_curry_test():
    assert_iterables_equal(without([1, 2])([1, 2, 1, 3, 4]), [3, 4])
