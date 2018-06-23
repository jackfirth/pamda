from .join import join
from pyramda.private.asserts import assert_equal


def reduce_nocurry_test():
    assert_equal(join(" ", ["aa", "bb", "cc"]), "aa bb cc")


def reduce_curry_test():
    assert_equal(join(" ")(["aa", "bb", "cc"]), "aa bb cc")
