from pyramda.private.asserts import assert_iterables_equal
from .xprod import xprod


def uniq_nocurry_test():
    assert_iterables_equal(xprod([1, 2], ['a', 'b']), [
                           [1, 'a'], [2, 'a'], [1, 'b'], [2, 'b']])


def take_curry_test():
    assert_iterables_equal(xprod([1, 2])(['a', 'b']), [
                           [1, 'a'], [2, 'a'], [1, 'b'], [2, 'b']])
