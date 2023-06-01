'''
тесты для встроенных функций filter, map, sorted
'''


def test_filter():
    assert list(filter(lambda x: x > 3, [1, 2, 3, 4, 5])) == [4, 5]
    assert list(filter(lambda x: x <= 3, [1, 2, 3, 4, 5])) == [1, 2, 3]


def test_map():
    assert list(map(lambda x: x * 2 + 3, [10, 15, 21, 33, 42, 55])) == [23, 33, 45, 69, 87, 113]
    assert list(map(lambda x: x ** 2, range(6))) == [0, 1, 4, 9, 16, 25]


def test_sorted():
    assert sorted([5, 2, 7, 2, 1, 8]) == [1, 2, 2, 5, 7, 8]
    assert sorted(['q','w','e','r','t','y']) == ['e', 'q', 'r', 't', 'w', 'y']
