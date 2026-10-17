import random

from ch21_mergesort import (count_inversions, hybrid_sort, merge, merge_comparisons, mergesort, mergesort_bottom_up,
                            mergesort_by, mergesort_in_place)


def rand_lists(n=60, seed=0):
    rng = random.Random(seed)
    return [[rng.randint(-30, 30) for _ in range(rng.randint(0, 40))] for _ in range(n)]


def test_ex_21_1():
    assert merge([1, 4, 9], [2, 3, 10, 11]) == [1, 2, 3, 4, 9, 10, 11] and merge([], [1]) == [1]
    assert merge([], []) == []


def test_ex_21_2():
    assert merge_comparisons([1, 2, 3], [4, 5, 6])[1] == 3 and merge_comparisons([1, 3, 5], [2, 4, 6])[1] == 5
    assert merge_comparisons([1, 3, 5], [2, 4, 6])[0] == [1, 2, 3, 4, 5, 6]


def test_ex_21_3():
    assert mergesort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]
    for data in rand_lists(seed=1):
        assert mergesort(data) == sorted(data)


def test_ex_21_4():
    a = [5, 2, 4, 6, 1, 3]
    mergesort_in_place(a)
    assert a == [1, 2, 3, 4, 5, 6]
    for data in rand_lists(seed=2):
        a = list(data)
        mergesort_in_place(a)
        assert a == sorted(data)


def test_ex_21_5():
    for data in rand_lists(seed=3):
        assert mergesort_bottom_up(data) == sorted(data)


def test_ex_21_6():
    assert count_inversions([2, 4, 1, 3, 5]) == 3 and count_inversions([5, 4, 3, 2, 1]) == 10
    for data in rand_lists(seed=4):
        brute = sum(1 for i in range(len(data)) for j in range(i + 1, len(data)) if data[i] > data[j])
        assert count_inversions(data) == brute


def test_ex_21_7():
    records = [("ann", 3), ("bo", 1), ("cy", 3), ("di", 1)]
    assert mergesort_by(records, key=lambda r: r[1]) == [('bo', 1), ('di', 1), ('ann', 3), ('cy', 3)]


def test_ex_21_8():
    assert hybrid_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], cutoff=4) == list(range(10))
    for data in rand_lists(seed=5):
        assert hybrid_sort(data, 4) == sorted(data)
