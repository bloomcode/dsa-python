import pytest
from ch19_space import (dup_nested, dup_set, dup_sort_in_place, is_palindrome_clean, recursion_limit, reverse_copy,
                        sum_to_iterative, sum_to_recursive, uppercase_copy, uppercase_in_place)


def test_ex_19_1():
    words = ['amy', 'bob']
    assert uppercase_copy(words) == ['AMY', 'BOB'] and words == ['amy', 'bob']
    assert uppercase_in_place(words) is words and words == ['AMY', 'BOB']


def test_ex_19_2():
    for fn in (dup_nested, dup_set, dup_sort_in_place):
        assert fn([3, 1, 4, 1]) and not fn([3, 1, 4])


def test_ex_19_3():
    assert sum_to_iterative(50_000) == 1250025000 and recursion_limit() >= 1000
    with pytest.raises(RecursionError):
        sum_to_recursive(50_000)
    assert sum_to_recursive(100) == 5050


def test_ex_19_4():
    original = [1, 2, 3]
    assert reverse_copy(original) == [3, 2, 1] and original == [1, 2, 3]


def test_ex_19_5():
    assert is_palindrome_clean('A man, a plan, a canal: Panama') and not is_palindrome_clean('ab')
