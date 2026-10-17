import pytest
from ch14_linked_lists import DoublyLinkedList, LinkedList, LinkedQueue, delete_node

L = LinkedList.from_list


def test_ex_14_1():
    assert L([1, 2, 3]).to_list() == [1, 2, 3] and len(L([1, 2, 3])) == 3 and len(L([])) == 0
    lst = L([7])
    assert lst.head.data == 7 and lst.head.next is None


def test_ex_14_2():
    lst = L([10, 20, 30])
    assert lst.read(2) == 30 and lst.read(5) is None and lst.read(0) == 10


def test_ex_14_3():
    lst = L([10, 20, 30])
    assert lst.index_of(20) == 1 and lst.index_of(99) is None


def test_ex_14_4():
    lst = L([2, 3])
    lst.insert_at_start(1)
    assert lst.to_list() == [1, 2, 3]
    lst = L([])
    lst.insert_at_start(1)
    assert lst.to_list() == [1]


def test_ex_14_5():
    lst = L([1, 2])
    lst.insert_at_end(3)
    assert lst.to_list() == [1, 2, 3]
    lst = L([])
    lst.insert_at_end(1)
    assert lst.to_list() == [1]


def test_ex_14_6():
    lst = L([1, 2, 4])
    lst.insert_at(2, 3)
    assert lst.to_list() == [1, 2, 3, 4]
    lst.insert_at(4, 5)
    lst.insert_at(0, 0)
    assert lst.to_list() == [0, 1, 2, 3, 4, 5]
    with pytest.raises(IndexError):
        L([1]).insert_at(3, 9)


def test_ex_14_7():
    lst = L([1, 2, 3])
    assert lst.delete_at_start() == 1 and lst.to_list() == [2, 3]
    assert L([]).delete_at_start() is None


def test_ex_14_8():
    lst = L([1, 2, 3])
    assert lst.delete_at_end() == 3 and lst.to_list() == [1, 2]
    lst = L([1])
    assert lst.delete_at_end() == 1 and lst.to_list() == []


def test_ex_14_9():
    lst = L([1, 2, 9, 3])
    assert lst.delete_at(2) == 9 and lst.to_list() == [1, 2, 3]
    assert lst.delete_at(2) == 3 and lst.to_list() == [1, 2]
    with pytest.raises(IndexError):
        lst.delete_at(2)
    with pytest.raises(IndexError):
        L([]).delete_at(0)


def test_ex_14_10():
    lst = L([4, 5, 4])
    assert lst.delete_value(4) and lst.to_list() == [5, 4]
    assert lst.delete_value(4) and lst.to_list() == [5] and not lst.delete_value(7)


def test_ex_14_11():
    assert L([1, 2, 3, 4, 5]).last() == 5 and L([1, 2, 3, 4, 5]).middle() == 3
    assert L([1, 2, 3, 4]).middle() == 3 and L([]).middle() is None


def test_ex_14_12():
    lst = L([1, 2, 3])
    lst.reverse()
    assert lst.to_list() == [3, 2, 1]
    empty = L([])
    empty.reverse()
    assert empty.to_list() == []


def test_ex_14_13():
    lst = L(['a', 'b', 'c', 'd'])
    delete_node(lst.head.next)
    assert lst.to_list() == ['a', 'c', 'd']


def test_ex_14_14():
    cyc = L([1, 2, 3, 4])
    assert not cyc.has_cycle()
    cyc.head.next.next.next.next = cyc.head.next
    assert cyc.has_cycle()
    assert not L([]).has_cycle()


def test_ex_14_15():
    d = DoublyLinkedList()
    d.insert_at_end(2)
    d.insert_at_start(1)
    d.insert_at_end(3)
    assert d.to_list() == [1, 2, 3] and d.to_list_reversed() == [3, 2, 1]
    assert d.delete_at_end() == 3 and d.delete_at_start() == 1 and d.to_list() == [2]
    assert d.delete_at_end() == 2 and d.head is None and d.tail is None and d.delete_at_start() is None


def test_ex_14_16():
    q = LinkedQueue()
    for v in (1, 2, 3):
        q.enqueue(v)
    assert q.dequeue() == 1 and q.read() == 2
