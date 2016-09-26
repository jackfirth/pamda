from .reject import reject
from pyramda.private.asserts import assert_equal

is_even = lambda x: x % 2 == 0

is_odd = lambda x: x % 2 == 1


def non_curried_reject_test():
    assert_equal(
        reject(is_even, [0, 1, 2, 3]),
        [1, 3]
    )

    assert_equal(
        reject(is_odd, [0, 1, 2, 3]),
        [0, 2]
    )


def curried_reject_test():
    assert_equal(
        reject(is_even)([0, 1, 2, 3]),
        [1, 3]
    )

    assert_equal(
        reject(is_odd)([0, 1, 2, 3]),
        [0, 2]
    )
