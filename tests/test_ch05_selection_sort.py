import random

from ch05_selection_sort import bubble_counts, every_other, k_smallest, second_largest, selection_counts, selection_sort


def test_ex_5_1():
    rng = random.Random(1)
    data = [rng.randint(-50, 50) for _ in range(60)]
    assert selection_sort(list(data)) == sorted(data)
    assert selection_sort([]) == []


def test_ex_5_2():
    rev = list(range(10, 0, -1))
    assert bubble_counts(rev) == (45, 45) and selection_counts(rev) == (45, 5)


def test_ex_5_3():
    assert every_other([10, 11, 12, 13, 14]) == [10, 12, 14] and every_other([]) == []


def test_ex_5_4():
    assert second_largest([5, 1, 9, 7, 9]) == 7 and second_largest([3, 3]) is None
    assert second_largest([1, 2]) == 1 and second_largest([9, 8, 10]) == 9


def test_ex_5_5():
    assert k_smallest([8, 3, 5, 1, 9], 2) == [1, 3]
