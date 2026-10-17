import pytest
from ch08_hash_tables import (HashTable, first_duplicate, first_unique_char, group_anagrams, intersection, invert,
                              is_subset, missing_letter, most_common_word, two_sum_indices, word_counts)


def test_ex_8_1():
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


def test_ex_8_2():
    assert is_subset(['b', 'd'], ['a', 'b', 'c', 'd']) and not is_subset(['z'], ['a'])


def test_ex_8_3():
    assert intersection([1, 2, 3, 4, 5], [0, 2, 4, 6, 8]) == [2, 4]
    assert intersection([2, 2], [2]) == [2]


def test_ex_8_4():
    assert first_duplicate(['a', 'b', 'c', 'd', 'c', 'e', 'f']) == 'c'
    assert first_duplicate(['a']) is None


def test_ex_8_5():
    assert missing_letter('the quick brown box jumps over a lazy dog') == 'f'


def test_ex_8_6():
    assert first_unique_char('minimum') == 'n' and first_unique_char('aa') is None


def test_ex_8_7():
    assert word_counts('the cat and the hat') == {'the': 2, 'cat': 1, 'and': 1, 'hat': 1}
    assert most_common_word('the cat and the hat') == 'the'


def test_ex_8_8():
    assert group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']) == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]


def test_ex_8_9():
    assert two_sum_indices([2, 7, 11, 15], 9) == (0, 1) and two_sum_indices([1], 2) is None
    assert two_sum_indices([3, 3], 6) == (0, 1)


def test_ex_8_10():
    assert invert({'fries': 2, 'soda': 2, 'burger': 5}) == {2: ['fries', 'soda'], 5: ['burger']}
