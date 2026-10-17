import pytest
from ch41_hash_tables import (can_build, distinct_per_day, group_anagrams, HashTable, in_exactly_one, invert,
                              most_common_word, positions, same_pattern, two_sum_indices, word_counts)


def test_ex_41_1():
    t = HashTable(2)
    t.put('bad', 'evil')
    t.put('bad', 'awful')
    assert t.get('bad') == 'awful' and len(t) == 1
    for i in range(100):
        t.put(i, i * i)
    assert len(t) == 101 and t.get(42) == 1764 and len(t.buckets) >= 128
    assert 7 in t and t.delete(7) and 7 not in t and not t.delete(7)
    with pytest.raises(KeyError):
        t.get('missing')


def test_ex_41_2():
    assert can_build('abba', 'aabbc') and not can_build('abc', 'ab')
    assert can_build('', 'xyz') and not can_build('aa', 'a') and can_build('cab', 'bac')


def test_ex_41_3():
    assert in_exactly_one([1, 2, 3], [2, 3, 4]) == [1, 4]
    assert in_exactly_one([5, 5, 1], [1]) == [5] and in_exactly_one([], [2, 2]) == [2] and in_exactly_one([1], [1]) == []


def test_ex_41_4():
    assert distinct_per_day([1, 1, 1, 2], ['ana', 'bo', 'ana', 'ana']) == {1: 2, 2: 1}
    assert distinct_per_day([], []) == {} and distinct_per_day([7, 7], ['x', 'x']) == {7: 1}


def test_ex_41_5():
    assert same_pattern('egg', 'add') and not same_pattern('foo', 'bar')
    assert same_pattern('paper', 'title') and not same_pattern('ab', 'aa') and not same_pattern('aa', 'ab')
    assert not same_pattern('a', 'ab') and same_pattern('', '')


def test_ex_41_6():
    assert positions(['a', 'b', 'a']) == {'a': [0, 2], 'b': [1]}
    assert positions([]) == {} and positions(['x'] * 3) == {'x': [0, 1, 2]}


def test_ex_41_7():
    assert word_counts('the cat and the hat') == {'the': 2, 'cat': 1, 'and': 1, 'hat': 1}
    assert most_common_word('the cat and the hat') == 'the'


def test_ex_41_8():
    assert group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


def test_ex_41_9():
    assert two_sum_indices([2, 7, 11, 15], 9) == (0, 1) and two_sum_indices([1], 2) is None
    assert two_sum_indices([3, 3], 6) == (0, 1)


def test_ex_41_10():
    assert invert({'fries': 2, 'soda': 2, 'burger': 5}) == {2: ['fries', 'soda'], 5: ['burger']}
