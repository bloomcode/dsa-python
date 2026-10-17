import random
from ch52_heaps import DeadlineQueue, heap_sort, is_max_heap, MaxHeap, merge_k_sorted, top_k


def test_ex_52_1():
    assert MaxHeap.left_child(0) == 1 and MaxHeap.right_child(0) == 2 and MaxHeap.parent(4) == 1
    h = MaxHeap()
    assert len(h) == 0
    h.data = [9, 5, 3]
    assert h.root() == 9 and h.last() == 3 and len(h) == 3


def test_ex_52_2():
    h = MaxHeap()
    for v in (3, 9, 5, 12):
        h.insert(v)
    assert h.root() == 12 and len(h) == 4
    assert all(h.data[MaxHeap.parent(i)] >= h.data[i] for i in range(1, len(h.data)))


def test_ex_52_3():
    h = MaxHeap()
    for v in (3, 9, 5, 12):
        h.insert(v)
    assert [h.delete() for _ in range(5)] == [12, 9, 5, 3, None]


def test_ex_52_4():
    rng = random.Random(1)
    data = [rng.randint(-100, 100) for _ in range(200)]
    assert heap_sort(data) == sorted(data) and heap_sort([]) == []


def test_ex_52_5():
    q = DeadlineQueue()
    q.add('report', 5)
    q.add('backup', 2)
    q.add('email', 2)
    assert [q.next_job() for _ in range(4)] == ['backup', 'email', 'report', None]
    q.add('late', 9)
    q.add('soon', 1)
    assert q.next_job() == 'soon'


def test_ex_52_6():
    assert top_k([3, 1, 9, 7, 5, 8], 3) == [9, 8, 7]


def test_ex_52_7():
    assert is_max_heap([100, 88, 25, 87, 16]) and not is_max_heap([10, 20]) and is_max_heap([])


def test_ex_52_8():
    assert merge_k_sorted([[1, 4, 7], [2, 5], [0, 9], []]) == [0, 1, 2, 4, 5, 7, 9]
    assert merge_k_sorted([]) == []
