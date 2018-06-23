from .uniq import uniq
from pyramda.private.asserts import assert_iterables_equal


def uniq_nocurry_test():
    assert_iterables_equal(uniq([1, 2, 3, 3, 4]), [1, 2, 3, 4])
