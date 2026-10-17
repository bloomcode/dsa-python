import random

from ch32_bit_vectors import BitVector, BoolArraySet, IntBitSet, first_duplicate, missing, space_report


def vector(size, members):
    bv = BitVector(size)
    for x in members:
        bv.add(x)
    return bv


def test_ex_32_1():
    s = BoolArraySet(10)
    s.add(3)
    s.add(7)
    s.remove(3)
    s.add(7)
    assert 7 in s and 3 not in s and len(s) == 1


def test_ex_32_2():
    bv = BitVector(100)
    bv.add(42)
    assert 42 in bv and 41 not in bv and bv.data[5] == 4
    bv.remove(42)
    assert 42 not in bv
    bv.remove(42)
    assert 42 not in bv


def test_ex_32_3():
    bv = vector(100, (1, 5, 99))
    assert len(bv) == 3
    bv.add(5)
    assert len(bv) == 3 and len(BitVector(10)) == 0


def test_ex_32_4():
    a, b = vector(10, (1, 2, 3)), vector(10, (2, 3, 4))
    u, i, d = a.union(b), a.intersection(b), a.difference(b)
    assert [x for x in range(10) if x in u] == [1, 2, 3, 4]
    assert [x for x in range(10) if x in i] == [2, 3]
    assert [x for x in range(10) if x in d] == [1]


def test_ex_32_5():
    assert list(vector(70, (9, 2, 63))) == [2, 9, 63]
    members = set(random.Random(3).sample(range(5000), 700))
    big = vector(5000, members)
    assert list(big) == sorted(members) and len(big) == 700


def test_ex_32_6():
    rep = space_report(100_000)
    assert rep["bit_vector"] == 12500 and rep["bit_vector"] * 50 < rep["bool_list"] < rep["set"]


def test_ex_32_7():
    assert first_duplicate([4, 9, 1, 9, 4], 10) == 9 and first_duplicate([1, 2, 3], 10) is None


def test_ex_32_8():
    x, y = IntBitSet([1, 5]), IntBitSet([5, 7])
    assert list(x | y) == [1, 5, 7] and len(x & y) == 1 and 5 in x and 7 not in x


def test_ex_32_9():
    assert missing([0, 3, 1, 6], 7) == [2, 4, 5] and missing(list(range(5)), 5) == []
