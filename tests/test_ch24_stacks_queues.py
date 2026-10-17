from ch24_stacks_queues import (CircularQueue, Editor, eval_rpn, Queue, round_robin, simplify_path, Stack,
                                StackQueue, tags_balanced)


def test_ex_24_1():
    s = Stack()
    assert s.is_empty()
    for v in (1, 2, 3):
        s.push(v)
    assert s.read() == 3 and s.pop() == 3 and s.read() == 2 and len(s) == 2 and not s.is_empty()
    assert Stack().pop() is None


def test_ex_24_2():
    q = Queue()
    assert q.is_empty()
    for v in (1, 2, 3):
        q.enqueue(v)
    assert q.dequeue() == 1 and q.read() == 2 and len(q) == 2 and not q.is_empty()


def test_ex_24_3():
    assert tags_balanced('<p><b>hi</b></p>') and not tags_balanced('<p><b></p></b>')
    assert not tags_balanced('<p>') and not tags_balanced('</p>') and tags_balanced('plain text')
    assert tags_balanced('<a><b></b><c>x</c></a>') and not tags_balanced('<a></a></a>')


def test_ex_24_4():
    assert simplify_path('/a/./b/../c/') == '/a/c' and simplify_path('/../') == '/'
    assert simplify_path('/home//user/') == '/home/user' and simplify_path('/a/b/../../..') == '/'
    assert simplify_path('/x/y/./z') == '/x/y/z'


def test_ex_24_5():
    assert round_robin(['a', 'b', 'c'], [3, 1, 2], 1) == ['b', 'c', 'a']
    assert round_robin(['a', 'b', 'c'], [3, 1, 2], 5) == ['a', 'b', 'c']
    assert round_robin(['x', 'y'], [4, 4], 2) == ['x', 'y'] and round_robin([], [], 3) == []


def test_ex_24_6():
    sq = StackQueue()
    sq.enqueue(1)
    sq.enqueue(2)
    assert sq.dequeue() == 1
    sq.enqueue(3)
    assert sq.dequeue() == 2 and sq.dequeue() == 3 and sq.dequeue() is None


def test_ex_24_7():
    assert eval_rpn(['3', '4', '+', '2', '*']) == 14
    assert eval_rpn(['10', '4', '-']) == 6 and eval_rpn(['9', '2', '/']) == 4.5


def test_ex_24_8():
    e = Editor()
    e.type('a')
    e.type('b')
    assert e.undo() == 'a' and e.redo() == 'ab'
    e.undo()
    e.type('c')
    assert e.text == 'ac' and e.redo() == 'ac' and e.undo() == 'a' and e.undo() == '' and e.undo() == ''


def test_ex_24_9():
    c = CircularQueue(3)
    assert all(c.enqueue(v) for v in (1, 2, 3)) and not c.enqueue(4)
    assert c.dequeue() == 1 and c.enqueue(4) and c.data[0] == 4
    assert [c.dequeue() for _ in range(4)] == [2, 3, 4, None]
