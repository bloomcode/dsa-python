import pytest
from ch23_linked_lists import DoublyLinkedList, LinkedList, LinkedQueue, merge_sorted_lists


L = LinkedList.from_list


def test_ex_23_1():
    assert L([1, 2, 3]).to_list() == [1, 2, 3] and len(L([1, 2, 3])) == 3 and len(L([])) == 0
    lst = L([7])
    assert lst.head.data == 7 and lst.head.next is None


def test_ex_23_2():
    lst = L([10, 20, 30])
    assert lst.read(2) == 30 and lst.read(5) is None and lst.read(0) == 10


def test_ex_23_3():
    lst = L([10, 20, 30])
    assert lst.index_of(20) == 1 and lst.index_of(99) is None


def test_ex_23_4():
    lst = L([2, 3])
    lst.insert_at_start(1)
    assert lst.to_list() == [1, 2, 3]
    lst = L([])
    lst.insert_at_start(1)
    assert lst.to_list() == [1]


def test_ex_23_5():
    lst = L([1, 2])
    lst.insert_at_end(3)
    assert lst.to_list() == [1, 2, 3]
    lst = L([])
    lst.insert_at_end(1)
    assert lst.to_list() == [1]


def test_ex_23_6():
    lst = L([1, 2, 4])
    lst.insert_at(2, 3)
    assert lst.to_list() == [1, 2, 3, 4]
    lst.insert_at(4, 5)
    lst.insert_at(0, 0)
    assert lst.to_list() == [0, 1, 2, 3, 4, 5]
    with pytest.raises(IndexError):
        L([1]).insert_at(3, 9)


def test_ex_23_7():
    lst = L([1, 2, 3])
    assert lst.delete_at_start() == 1 and lst.to_list() == [2, 3]
    assert L([]).delete_at_start() is None


def test_ex_23_8():
    lst = L([1, 2, 3])
    assert lst.delete_at_end() == 3 and lst.to_list() == [1, 2]
    lst = L([1])
    assert lst.delete_at_end() == 1 and lst.to_list() == []


def test_ex_23_9():
    lst = L([1, 2, 9, 3])
    assert lst.delete_at(2) == 9 and lst.to_list() == [1, 2, 3]
    assert lst.delete_at(2) == 3 and lst.to_list() == [1, 2]
    with pytest.raises(IndexError):
        lst.delete_at(2)
    with pytest.raises(IndexError):
        L([]).delete_at(0)


def test_ex_23_10():
    lst = L([4, 5, 4])
    assert lst.delete_value(4) and lst.to_list() == [5, 4]
    assert lst.delete_value(4) and lst.to_list() == [5] and not lst.delete_value(7)


def test_ex_23_11():
    lst = L([1, 2, 3, 4, 5])
    second = lst.split_half()
    assert lst.to_list() == [1, 2, 3] and second.to_list() == [4, 5]
    even = L([1, 2, 3, 4])
    assert even.split_half().to_list() == [3, 4] and even.to_list() == [1, 2]
    one, empty = L([7]), L([])
    assert one.split_half().to_list() == [] and one.to_list() == [7] and empty.split_half().to_list() == []


def test_ex_23_12():
    lst = L([1, 2, 3])
    lst.reverse()
    assert lst.to_list() == [3, 2, 1]
    empty = L([])
    empty.reverse()
    assert empty.to_list() == []


def test_ex_23_13():
    a, b = L([1, 4, 7]), L([2, 3, 9])
    first_b = b.head
    merged = merge_sorted_lists(a, b)
    assert merged.to_list() == [1, 2, 3, 4, 7, 9] and merged.head.next is first_b
    assert merge_sorted_lists(L([]), L([5])).to_list() == [5] and merge_sorted_lists(L([2, 2]), L([2])).to_list() == [2, 2, 2]
    assert merge_sorted_lists(L([]), L([])).to_list() == []


def test_ex_23_14():
    cyc = L([1, 2, 3, 4])
    assert not cyc.has_cycle()
    cyc.head.next.next.next.next = cyc.head.next
    assert cyc.has_cycle()
    assert not L([]).has_cycle()


def test_ex_23_15():
    d = DoublyLinkedList()
    d.insert_at_end(2)
    d.insert_at_start(1)
    d.insert_at_end(3)
    assert d.to_list() == [1, 2, 3] and d.to_list_reversed() == [3, 2, 1]
    assert d.delete_at_end() == 3 and d.delete_at_start() == 1 and d.to_list() == [2]
    assert d.delete_at_end() == 2 and d.head is None and d.tail is None and d.delete_at_start() is None


def test_ex_23_16():
    q = LinkedQueue()
    for v in (1, 2, 3):
        q.enqueue(v)
    assert q.dequeue() == 1 and q.read() == 2
