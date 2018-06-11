from .zip_obj import zip_obj
from pyramda.private.asserts import assert_iterables_equal


def uniq_nocurry_test():
    assert_iterables_equal(zip_obj(['a', 'b', 'c'], [1, 2, 3]), {'a': 1, 'b': 2, 'c': 3})


def take_curry_test():
    assert_iterables_equal(zip_obj(['a', 'b', 'c'])([1, 2, 3]), {'a': 1, 'b': 2, 'c': 3})
