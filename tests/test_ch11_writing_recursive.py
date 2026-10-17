from ch11_writing_recursive import (anagrams, count_x, double_in_place, index_of_x, reverse, select_evens,
                                   staircase, subsets, total_chars, triangular, unique_paths)


def test_ex_11_1():
    assert double_in_place([1, 2, 3]) == [2, 4, 6]


def test_ex_11_2():
    assert reverse('abcde') == 'edcba' and reverse('') == ''


def test_ex_11_3():
    assert count_x('axbxcxd') == 3 and count_x('') == 0


def test_ex_11_4():
    assert total_chars(['ab', 'c', 'def', 'ghij']) == 10


def test_ex_11_5():
    assert select_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_ex_11_6():
    assert triangular(7) == 28 and triangular(1) == 1


def test_ex_11_7():
    assert index_of_x('abcdefghijklmnopqrstuvwxyz') == 23 and index_of_x('abc') == -1


def test_ex_11_8():
    assert staircase(3) == 4 and staircase(5) == 13


def test_ex_11_9():
    assert sorted(anagrams('abc')) == sorted(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    assert len(anagrams('abcdef')) == 720


def test_ex_11_10():
    assert unique_paths(3, 7) == 28


def test_ex_11_11():
    assert sorted(map(sorted, subsets([1, 2]))) == [[], [1], [1, 2], [2]]
    assert len(subsets([1, 2, 3, 4])) == 16
