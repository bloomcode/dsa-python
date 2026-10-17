from ch73_greedy_transforms import (can_reach_end, has_pair_with_difference, lone_value, longest_unique_run,
                                    max_meetings, RangeSum, rooms_needed, top_k_frequent, window_with_sum)


def test_ex_73_1():
    assert has_pair_with_difference([1, 8, 4, 11], 3) and not has_pair_with_difference([1, 5], 3)
    assert has_pair_with_difference([3, 3], 0) and not has_pair_with_difference([3], 0) and has_pair_with_difference([10, -2], 12)


def test_ex_73_2():
    assert window_with_sum([2, 4, 3, 5, 1], 8) == (2, 3) and window_with_sum([1, 2], 7) is None
    assert window_with_sum([5], 5) == (0, 0) and window_with_sum([1, 2, 3], 6) == (0, 2) and window_with_sum([], 1) is None


def test_ex_73_3():
    assert can_reach_end([2, 3, 1, 1, 4]) and not can_reach_end([3, 2, 1, 0, 4])
    assert can_reach_end([0]) and not can_reach_end([0, 1]) and can_reach_end([1, 1, 1])


def test_ex_73_4():
    assert rooms_needed([[9, 11], [10, 12], [11, 13], [9, 10]]) == 2
    assert rooms_needed([]) == 0 and rooms_needed([[1, 5], [2, 6], [3, 7]]) == 3 and rooms_needed([[1, 2], [2, 3]]) == 1


def test_ex_73_5():
    assert max_meetings([[1, 4], [3, 5], [0, 6], [5, 7], [8, 9], [5, 9]]) == 3
    assert max_meetings([]) == 0 and max_meetings([[1, 10], [2, 3], [3, 4], [4, 5]]) == 3 and max_meetings([[1, 2], [1, 2]]) == 1


def test_ex_73_6():
    r = RangeSum([3, 1, 4, 1, 5])
    assert r.total(1, 3) == 6 and r.total(0, 4) == 14 and r.total(2, 2) == 4 and r.total(0, 0) == 3
    assert RangeSum([-2, 2]).total(0, 1) == 0


def test_ex_73_7():
    assert top_k_frequent(['b', 'a', 'b', 'c', 'a', 'b'], 2) == ['b', 'a']
    assert top_k_frequent(['x', 'y', 'z'], 2) == ['x', 'y'] and top_k_frequent(['q'], 5) == ['q'] and top_k_frequent([], 1) == []
    assert top_k_frequent(['m', 'n', 'n', 'm', 'o'], 3) == ['m', 'n', 'o']


def test_ex_73_8():
    assert lone_value([4, 1, 2, 1, 2]) == 4 and lone_value([7]) == 7 and lone_value([0, 9, 9]) == 0 and lone_value([-3, 5, 5]) == -3


def test_ex_73_9():
    assert longest_unique_run('abcadbe') == 5 and longest_unique_run('aaaa') == 1 and longest_unique_run('') == 0
    assert longest_unique_run('abba') == 2 and longest_unique_run('xyz') == 3 and longest_unique_run('tmmzuxt') == 5
