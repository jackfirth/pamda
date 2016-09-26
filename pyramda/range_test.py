from .range import range
from .iterable.map import fmap
from pyramda.private.asserts import assert_equal


def no_curry_range_test():
    assert_equal(
        fmap(lambda identity: identity, range(1, 4)),
        [1, 2, 3]
    )


def no_curry_range_test():
    assert_equal(
        fmap(lambda identity: identity, range(1, 4)),
        [1, 2, 3]
    )
