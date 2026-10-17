import random

from ch16_heaps import MaxHeap, TriageQueue, heap_sort, is_max_heap, merge_k_sorted, top_k


def test_ex_16_1():
    assert MaxHeap.left_child(0) == 1 and MaxHeap.right_child(0) == 2 and MaxHeap.parent(4) == 1
    h = MaxHeap()
    assert len(h) == 0
    h.data = [9, 5, 3]
    assert h.root() == 9 and h.last() == 3 and len(h) == 3


def test_ex_16_2():
    h = MaxHeap()
    for v in (3, 9, 5, 12):
        h.insert(v)
    assert h.root() == 12 and len(h) == 4
    assert all(h.data[MaxHeap.parent(i)] >= h.data[i] for i in range(1, len(h.data)))


def test_ex_16_3():
    h = MaxHeap()
    for v in (3, 9, 5, 12):
        h.insert(v)
    assert [h.delete() for _ in range(5)] == [12, 9, 5, 3, None]


def test_ex_16_4():
    rng = random.Random(1)
    data = [rng.randint(-100, 100) for _ in range(200)]
    assert heap_sort(data) == sorted(data) and heap_sort([]) == []


def test_ex_16_5():
    tq = TriageQueue()
    tq.admit('Ann', 3)
    tq.admit('Bo', 9)
    tq.admit('Cy', 9)
    assert [tq.next_patient() for _ in range(4)] == ['Bo', 'Cy', 'Ann', None]


def test_ex_16_6():
    assert top_k([3, 1, 9, 7, 5, 8], 3) == [9, 8, 7]


def test_ex_16_7():
    assert is_max_heap([100, 88, 25, 87, 16]) and not is_max_heap([10, 20]) and is_max_heap([])


def test_ex_16_8():
    assert merge_k_sorted([[1, 4, 7], [2, 5], [0, 9], []]) == [0, 1, 2, 4, 5, 7, 9]
    assert merge_k_sorted([]) == []
