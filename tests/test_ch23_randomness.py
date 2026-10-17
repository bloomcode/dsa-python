import random

from ch23_randomness import (bst_height, fisher_yates, fisher_yates_distribution, lcg, lcg_period, make_weighted_picker,
                             max_load_random, max_load_two_choices, naive_distribution, random_quicksort, reservoir,
                             sample_with_seed)


def test_ex_23_1():
    rng = random.Random(0)
    for _ in range(60):
        data = [rng.randint(-30, 30) for _ in range(rng.randint(0, 40))]
        assert random_quicksort(data, random.Random(3)) == sorted(data)
    assert random_quicksort(list(range(10)), random.Random(1)) == list(range(10))


def test_ex_23_2():
    assert sample_with_seed(42, range(100), 3) == sample_with_seed(42, range(100), 3)
    assert len(sample_with_seed(42, range(100), 3)) == 3


def test_ex_23_3():
    g = lcg(1, 5, 3, 16)
    assert [next(g) for _ in range(3)] == [8, 11, 10]
    assert lcg_period(1, 5, 3, 16) == 16


def test_ex_23_4():
    a = fisher_yates([1, 2, 3, 4, 5], random.Random(7))
    assert sorted(a) == [1, 2, 3, 4, 5]
    assert fisher_yates([1, 2, 3, 4, 5], random.Random(7)) == a


def test_ex_23_5():
    fy = fisher_yates_distribution(3)
    assert len(fy) == 6 and set(fy.values()) == {1}
    nv = naive_distribution(3)
    assert sum(nv.values()) == 27 and sorted(nv.values()) == [4, 4, 4, 5, 5, 5]
    assert set(fisher_yates_distribution(4).values()) == {1}


def test_ex_23_6():
    assert bst_height(list(range(200))) == 200
    keys = list(range(200))
    random.Random(3).shuffle(keys)
    assert bst_height(keys) < 30


def test_ex_23_7():
    s = reservoir(range(10**5), 3, random.Random(0))
    assert len(s) == 3 and len(set(s)) == 3
    firsts = [reservoir(range(10), 1, random.Random(i))[0] for i in range(5000)]
    assert all(350 < firsts.count(v) < 650 for v in range(10))


def test_ex_23_8():
    one = max_load_random(10000, 1000, random.Random(5))
    two = max_load_two_choices(10000, 1000, random.Random(5))
    assert two < one and two <= 14


def test_ex_23_9():
    pick = make_weighted_picker([1, 3, 6], random.Random(2))
    picks = [pick() for _ in range(10000)]
    assert 5600 < picks.count(2) < 6400 and set(picks) == {0, 1, 2}
