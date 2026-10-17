from ch72_dynamic_programming import (count_fib_calls, dice_ways_memo, fib_bottom_up, fib_memo, fib_naive, min_coins,
                                      min_max, tilings_memo)


def test_ex_72_1():
    assert fib_naive(10) == fib_memo(10) == fib_bottom_up(10) == 55
    assert fib_memo(80) == fib_bottom_up(80) == 23416728348467685
    assert fib_bottom_up(0) == 0 and fib_bottom_up(1) == 1


def test_ex_72_2():
    assert min_max([4, -2, 9, 0]) == (-2, 9) and min_max([7]) == (7, 7) and min_max([3, 3]) == (3, 3)
    assert min_max(list(range(60))) == (0, 59)


def test_ex_72_3():
    assert tilings_memo(10) == 28 and tilings_memo(60) == 5582216355 and tilings_memo(90) == 533352837917926
    assert [tilings_memo(n) for n in range(8)] == [1, 1, 1, 2, 3, 4, 6, 9]


def test_ex_72_4():
    assert dice_ways_memo(2, 7) == 6 and dice_ways_memo(3, 10) == 27 and dice_ways_memo(1, 7) == 0
    assert dice_ways_memo(20, 70) == 189456975899496 and dice_ways_memo(10, 35) == 4395456


def test_ex_72_5():
    assert count_fib_calls(10) == (177, 19)


def test_ex_72_6():
    assert min_coins([1, 5, 10, 25], 63) == 6 and min_coins([2], 3) == -1
    assert min_coins([1, 3, 4], 6) == 2 and min_coins([1], 0) == 0
