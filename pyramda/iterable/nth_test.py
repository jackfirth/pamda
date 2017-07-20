from .nth import nth
from pyramda.private.asserts import assert_equal


def no_curry_nth_test():
    assert_equal(nth(1, [41, 42]), 42)


def negative_offset_test():
    assert_equal(nth(-1, [41, 42]), 42)


def curry_nth_test():
    assert_equal(nth(1)([41, 42]), 42)
