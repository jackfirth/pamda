from .map import map
from pyramda.private.asserts import assert_iterables_equal, assert_equal


def add1(x):
    return x + 1


def map_no_curry_test():
    assert_iterables_equal(map(add1, [1, 2, 3]), [2, 3, 4])


def map_curry_test():
    assert_iterables_equal(map(add1)([1, 2, 3]), [2, 3, 4])


class AFunctor(object):
    def __init__(self, value):
        self.value = value

    def map(self, f):
        return AFunctor(f(self.value))

    def get_val(self):
        return self.value


def no_curry_map_functor_test():
    container = AFunctor(41)
    with_f_applied = map(add1, container)
    assert_equal(with_f_applied.get_val(), 42)


def curry_map_functor_test():
    container = AFunctor(41)
    add1_to_contained_val = map(add1)
    assert_equal(add1_to_contained_val(container).get_val(), 42)
