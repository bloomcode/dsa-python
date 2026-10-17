from ch10_recursion import all_directories, countdown, factorial, flatten, numbers_between, power, sum_recursive


def test_ex_10_1():
    assert countdown(3) == [3, 2, 1, 0] and countdown(0) == [0]


def test_ex_10_2():
    assert factorial(5) == 120 and factorial(0) == 1


def test_ex_10_3():
    assert sum_recursive([1, 2, 3, 4]) == 10 and sum_recursive([]) == 0


def test_ex_10_4():
    assert flatten([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5] and flatten([]) == []


def test_ex_10_5():
    assert power(2, 10) == 1024 and power(3, 0) == 1 and power(5, 3) == 125


def test_ex_10_6():
    assert all_directories({'docs': {'old': {}, 'a.txt': None}, 'src': {}}) == ['/docs', '/docs/old', '/src']


def test_ex_10_7():
    assert numbers_between(3, 6) == [3, 4, 5, 6]
