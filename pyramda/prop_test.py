from .prop import prop
from pyramda.private.asserts import assert_equal


def no_curry_dict_prop_test():
    assert_equal(prop('a', {'a': 42}), 42)


def curry_dict_prop_test():
    assert_equal(prop('a')({'a': 42}), 42)


class Foo(object):
    bar = 'baz'


def no_curry_obj_prop_test():
    assert_equal(prop('bar', Foo()), 'baz')


def curry_obj_prop_test():
    assert_equal(prop('bar')(Foo()), 'baz')
