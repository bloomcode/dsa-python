from ch20_optimization import (are_anagrams, has_increasing_triplet, has_two_sum, longest_consecutive, max_profit,
                               max_subarray_sum, missing_number, sort_temperatures, sum_swap)


def test_ex_20_1():
    assert has_two_sum([2, 0, 4, 1, 7, 9], 10) and not has_two_sum([2, 0, 4, 1, 7, 9], 100)
    assert not has_two_sum([5], 10)


def test_ex_20_2():
    assert sum_swap([5, 3, 2, 9, 1], [1, 12, 5]) == (2, 0) and sum_swap([1], [2]) is None


def test_ex_20_3():
    assert max_subarray_sum([3, -4, 4, -3, 5, -9]) == 6 and max_subarray_sum([-3, -1, -2]) == -1


def test_ex_20_4():
    assert has_increasing_triplet([22, 25, 21, 18, 19.6, 17, 16, 20.5]) and not has_increasing_triplet([5, 4, 3])


def test_ex_20_5():
    assert max_profit([10, 7, 5, 8, 11, 2, 6]) == 6 and max_profit([5, 4, 3]) == 0


def test_ex_20_6():
    assert are_anagrams('listen', 'silent') and not are_anagrams('aab', 'abb')


def test_ex_20_7():
    temps = [98.6, 98.0, 97.1, 99.0, 98.9, 97.8, 98.5, 98.2, 98.0, 97.1]
    assert sort_temperatures(temps) == sorted(temps)


def test_ex_20_8():
    assert missing_number([5, 2, 4, 1, 0]) == 3


def test_ex_20_9():
    assert longest_consecutive([10, 5, 12, 3, 55, 30, 4, 11, 2]) == 4 and longest_consecutive([]) == 0
