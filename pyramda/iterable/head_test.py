from .head import head
from pyramda.private.asserts import assert_equal


def head_test():
    assert_equal(head([42, 43, 44]), 42)
