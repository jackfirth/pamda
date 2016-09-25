from .tail import tail
from pyramda.private.asserts import assert_equal


def tail_test():
    assert_equal(tail([42, 43, 44]), [43, 44])
