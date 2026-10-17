from ch12_dynamic_programming import (count_fib_calls, fib_bottom_up, fib_memo, fib_naive, max_recursive, min_coins,
                                      staircase_memo, unique_paths_memo)


def test_ex_12_1():
    assert fib_naive(10) == fib_memo(10) == fib_bottom_up(10) == 55
    assert fib_memo(80) == fib_bottom_up(80) == 23416728348467685
    assert fib_bottom_up(0) == 0 and fib_bottom_up(1) == 1


def test_ex_12_2():
    assert max_recursive([1, 2, 3, 4]) == 4 and max_recursive([9, 2]) == 9


def test_ex_12_3():
    assert staircase_memo(5) == 13 and staircase_memo(50) > 0


def test_ex_12_4():
    assert unique_paths_memo(3, 7) == 28 and unique_paths_memo(18, 18) == 2333606220


def test_ex_12_5():
    assert count_fib_calls(10) == (177, 19)


def test_ex_12_6():
    assert min_coins([1, 5, 10, 25], 63) == 6 and min_coins([2], 3) == -1
    assert min_coins([1, 3, 4], 6) == 2 and min_coins([1], 0) == 0
