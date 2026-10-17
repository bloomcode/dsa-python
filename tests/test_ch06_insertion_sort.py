import random

from ch06_insertion_sort import insert_sorted, insertion_sort, insertion_sort_steps, intersection_nested, merge_sorted


def test_ex_6_1():
    rng = random.Random(1)
    data = [rng.randint(-50, 50) for _ in range(60)]
    assert insertion_sort(list(data)) == sorted(data)
    assert insertion_sort([]) == []


def test_ex_6_2():
    assert insertion_sort_steps(list(range(100))) == 99
    assert insertion_sort_steps(list(range(100, 0, -1))) == 9900
    assert 99 < insertion_sort_steps(random.Random(2).sample(range(100), 100)) < 9900


def test_ex_6_3():
    assert intersection_nested([3, 1, 4, 2], [4, 5, 3, 6]) == [3, 4]
    assert intersection_nested([1, 2], [3]) == []


def test_ex_6_4():
    assert insert_sorted([1, 4, 9], 5) == [1, 4, 5, 9]
    assert insert_sorted([], 5) == [5] and insert_sorted([2], 1) == [1, 2]


def test_ex_6_5():
    assert merge_sorted([1, 4, 7], [2, 3, 9]) == [1, 2, 3, 4, 7, 9]
    assert merge_sorted([], [1]) == [1]
