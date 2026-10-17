import random

from ch04_bubble_sort import (bubble_sort, bubble_sort_optimized, greatest_linear, greatest_quadratic,
                              has_duplicate_linear, has_duplicate_quadratic, is_sorted)


def random_data(seed):
    rng = random.Random(seed)
    return [rng.randint(-50, 50) for _ in range(60)]


def test_ex_4_1():
    assert bubble_sort([4, 2, 7, 1, 3]) == [1, 2, 3, 4, 7]
    data = random_data(1)
    assert bubble_sort(list(data)) == sorted(data)
    assert bubble_sort([]) == []


def test_ex_4_2():
    data = random_data(2)
    assert bubble_sort_optimized(list(data))[0] == sorted(data)
    assert bubble_sort_optimized([1, 2, 3, 4]) == ([1, 2, 3, 4], 1)
    assert bubble_sort_optimized([4, 3, 2, 1])[1] == 3
    assert bubble_sort_optimized([]) == ([], 0)


def test_ex_4_3():
    assert has_duplicate_quadratic([1, 5, 3, 9, 1, 4]) and not has_duplicate_quadratic([1, 2, 3])


def test_ex_4_4():
    assert has_duplicate_linear([1, 5, 3, 9, 1, 4]) and not has_duplicate_linear([1, 2, 3])


def test_ex_4_5():
    assert greatest_quadratic([3, 9, 2, 7]) == 9 == greatest_linear([3, 9, 2, 7])
    assert greatest_quadratic([-4]) == -4 == greatest_linear([-4])


def test_ex_4_6():
    assert is_sorted([1, 2, 2, 5]) and not is_sorted([1, 3, 2])
    assert is_sorted([]) and is_sorted([7])
