from ch09_stacks_queues import (CircularQueue, Editor, PrintManager, Queue, Stack, StackQueue, eval_rpn, lint,
                                reverse_with_stack)


def test_ex_9_1():
    s = Stack()
    assert s.is_empty()
    for v in (1, 2, 3):
        s.push(v)
    assert s.read() == 3 and s.pop() == 3 and s.read() == 2 and len(s) == 2 and not s.is_empty()
    assert Stack().pop() is None


def test_ex_9_2():
    q = Queue()
    assert q.is_empty()
    for v in (1, 2, 3):
        q.enqueue(v)
    assert q.dequeue() == 1 and q.read() == 2 and len(q) == 2 and not q.is_empty()


def test_ex_9_3():
    assert lint('(var x = {y: [1, 2, 3]})') is None
    assert lint('(var x = 2;') == '( has no closing brace'
    assert lint('var x = 2)') == ') has no opening brace'
    assert lint('(var x = [1, 2, 3)]') == ') has mismatched opening brace'


def test_ex_9_4():
    assert reverse_with_stack('abcde') == 'edcba' and reverse_with_stack('') == ''


def test_ex_9_5():
    p = PrintManager()
    for d in ('First', 'Second', 'Third'):
        p.queue_job(d)
    assert p.run() == ['First', 'Second', 'Third']


def test_ex_9_6():
    sq = StackQueue()
    sq.enqueue(1)
    sq.enqueue(2)
    assert sq.dequeue() == 1
    sq.enqueue(3)
    assert sq.dequeue() == 2 and sq.dequeue() == 3 and sq.dequeue() is None


def test_ex_9_7():
    assert eval_rpn(['3', '4', '+', '2', '*']) == 14
    assert eval_rpn(['10', '4', '-']) == 6 and eval_rpn(['9', '2', '/']) == 4.5


def test_ex_9_8():
    e = Editor()
    e.type('a')
    e.type('b')
    assert e.undo() == 'a' and e.redo() == 'ab'
    e.undo()
    e.type('c')
    assert e.text == 'ac' and e.redo() == 'ac' and e.undo() == 'a' and e.undo() == '' and e.undo() == ''


def test_ex_9_9():
    c = CircularQueue(3)
    assert all(c.enqueue(v) for v in (1, 2, 3)) and not c.enqueue(4)
    assert c.dequeue() == 1 and c.enqueue(4) and c.data[0] == 4
    assert [c.dequeue() for _ in range(4)] == [2, 3, 4, None]
