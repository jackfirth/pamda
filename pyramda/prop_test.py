from .prop import prop
from pyramda.private.asserts import assert_equal


class TestObject:
    def __init__(self, val):
        self.val = val


test_object = TestObject("foo")


def prop_nocurry_test():
    assert_equal(prop("val", test_object), "foo")


def prop_curry_test():
    assert_equal(prop("val")(test_object), "foo")


def prop_nocurry_property_test():
    assert_equal(prop("val")({"val": "foo"}), "foo")
