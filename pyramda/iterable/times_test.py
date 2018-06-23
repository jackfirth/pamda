from .times import times
from pyramda.private.asserts import assert_iterables_equal


def uniq_nocurry_test():
    assert_iterables_equal(times(5), [1, 2, 3, 4])
