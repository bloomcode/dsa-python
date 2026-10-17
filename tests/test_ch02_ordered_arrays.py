from ch02_ordered_arrays import (OrderedArray, binary_search, binary_search_recursive, first_and_last,
                                 int_sqrt, linear_search_ordered, lower_bound, search_steps)


def test_ex_2_1():
    o = OrderedArray([3, 17, 80, 202])
    o.insert(75)
    assert o.items == [3, 17, 75, 80, 202]
    o.insert(1)
    o.insert(500)
    assert o.items == [1, 3, 17, 75, 80, 202, 500]
    e = OrderedArray()
    e.insert(4)
    assert e.items == [4]


def test_ex_2_2():
    assert linear_search_ordered([3, 17, 75, 80, 202], 22) == -1
    assert linear_search_ordered([3, 17, 75, 80, 202], 75) == 2
    assert linear_search_ordered([], 1) == -1


def check_binary_search(fn):
    assert fn([3, 17, 75, 80, 202], 80) == 3
    assert fn([1, 3, 5, 7, 9], 1) == 0 and fn([1, 3, 5, 7, 9], 9) == 4
    assert fn([1, 3, 5], 4) == -1 and fn([], 1) == -1


def test_ex_2_3():
    check_binary_search(binary_search)


def test_ex_2_4():
    check_binary_search(binary_search_recursive)


def test_ex_2_5():
    assert lower_bound([10, 20, 20, 30], 20) == 1
    assert lower_bound([10, 20, 20, 30], 25) == 3
    assert lower_bound([10, 20, 20, 30], 99) == 4
    assert lower_bound([10, 20], 5) == 0 and lower_bound([], 5) == 0


def test_ex_2_6():
    f = OrderedArray()
    for v in [5, 1, 4, 1, 9]:
        f.insert_fast(v)
    assert f.items == [1, 1, 4, 5, 9]
    g = OrderedArray([3, 17, 80, 202])
    g.insert_fast(75)
    assert g.items == [3, 17, 75, 80, 202]


def test_ex_2_7():
    assert first_and_last([1, 2, 2, 2, 5], 2) == (1, 3)
    assert first_and_last([1, 2, 5], 3) == (-1, -1)
    assert first_and_last([2.5, 2.5], 2.5) == (0, 1)


def test_ex_2_8():
    d = OrderedArray([2, 4, 6, 8])
    assert d.delete(4) and d.items == [2, 6, 8] and not d.delete(5)
    assert d.delete(8) and d.items == [2, 6]


def test_ex_2_9():
    assert search_steps(100) == (100, 7)
    assert search_steps(10_000) == (10000, 14)


def test_ex_2_10():
    assert int_sqrt(27) == 5 and int_sqrt(36) == 6 and int_sqrt(0) == 0 and int_sqrt(1) == 1
