import random

from ch13_quicksort import (has_duplicates_sorted, max_product_of_three, median, merge_sort, missing_number_sorted,
                            partition, quickselect, quicksort)


def random_lists(seed, n=200):
    rng = random.Random(seed)
    return [[rng.randint(0, 9) for _ in range(rng.randint(0, 25))] for _ in range(n)]


def test_ex_13_1():
    a = [0, 5, 2, 1, 6, 3]
    p = partition(a, 0, 5)
    assert p == 3 and all(x < 3 for x in a[:p]) and all(x > 3 for x in a[p + 1:])


def test_ex_13_2():
    for data in random_lists(1):
        assert quicksort(list(data)) == sorted(data)


def test_ex_13_3():
    assert quickselect([0, 50, 20, 10, 60, 30], 1) == 10
    rng = random.Random(2)
    for data in random_lists(3):
        if data:
            k = rng.randrange(len(data))
            assert quickselect(list(data), k) == sorted(data)[k]


def test_ex_13_4():
    assert has_duplicates_sorted([5, 9, 3, 2, 4, 5, 6]) and not has_duplicates_sorted([1, 2])


def test_ex_13_5():
    assert max_product_of_three([1, 10, 2, 6, 5, 3]) == 300
    assert max_product_of_three([-10, -10, 1, 3, 2]) == 300


def test_ex_13_6():
    assert missing_number_sorted([5, 2, 4, 1, 0]) == 3 and missing_number_sorted([0, 1, 2]) == 3


def test_ex_13_7():
    assert median([7, 1, 3]) == 3 and median([4, 1, 3, 2]) == 2.5


def test_ex_13_8():
    assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]
    for data in random_lists(4):
        assert merge_sort(data) == sorted(data)
