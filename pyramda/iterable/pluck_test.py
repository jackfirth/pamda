from .pluck import pluck


data = [{
    'a': 'a1',
    'b': 'b1'
}, {
    1: 1,
    2: 2
}, {
    'a': 'a2',
    'b': 'b2'
}]


def a_test():
    assert pluck('a', data) == ['a1', None, 'a2']


def one_test():
    assert pluck(1, data) == [None, 1, None]


def iterator_test():
    assert pluck(None, map(lambda x: x, [{None: 1}])) == [1]
