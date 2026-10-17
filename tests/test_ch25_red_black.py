import random

from ch25_red_black import BLACK, RED, RBNode, RedBlackTree, rotations_for


def tree(keys):
    t = RedBlackTree()
    for k in keys:
        t.insert(k)
    return t


def test_ex_25_1():
    t = RedBlackTree()
    assert t.root is t.NIL and t.NIL.color == BLACK
    x = RBNode(2, BLACK, t.NIL)
    a, y = RBNode(1, RED, t.NIL), RBNode(4, RED, t.NIL)
    b, c = RBNode(3, BLACK, t.NIL), RBNode(5, BLACK, t.NIL)
    x.left, x.right, a.parent, y.parent = a, y, x, x
    y.left, y.right, b.parent, c.parent = b, c, y, y
    t.root = x
    t.rotate_left(x)
    assert t.root is y and y.left is x and x.parent is y and y.parent is t.NIL
    assert x.left is a and x.right is b and b.parent is x and y.right is c
    t.rotate_right(y)
    assert t.root is x and x.right is y and y.parent is x and y.left is b and b.parent is y
    assert t.rotations == 2


def test_ex_25_2():
    t = tree(range(1, 8))
    assert t.root.key == 2 and t.root.color == BLACK and t.size == 7
    assert not t.insert(5) and t.size == 7


def test_ex_25_3():
    t = RedBlackTree()
    for k in range(1, 8):
        t.insert(k)
        t.validate()
    assert tree(range(1, 1001)).validate() > 0


def test_ex_25_4():
    t = tree([5, 2, 8, 1])
    assert t.contains(8) and not t.contains(3) and t.inorder() == [1, 2, 5, 8]
    assert tree(range(1, 8)).inorder() == list(range(1, 8))


def test_ex_25_5():
    assert tree(range(1, 8)).height() == 4
    t = tree(range(1, 1001))
    assert t.height() <= t.height_bound() and t.height() <= 19


def test_ex_25_6():
    t = tree([20, 10, 30, 25])
    assert t.minimum().key == 10 and t.maximum() == 30
    assert t.successor(20) == 25 and t.successor(30) is None and t.successor(10) == 20


def test_ex_25_7():
    assert rotations_for(range(1000)) < 1000


def test_ex_25_8():
    rng = random.Random(11)
    for _ in range(20):
        t, keys = RedBlackTree(), set()
        for _ in range(200):
            k = rng.randrange(300)
            if rng.random() < 0.6:
                t.insert(k)
                keys.add(k)
            else:
                assert t.delete(k) == (k in keys)
                keys.discard(k)
            t.validate()
        assert t.inorder() == sorted(keys) and t.size == len(keys)
    t = tree(range(1, 101))
    for k in range(2, 101, 2):
        t.delete(k)
    t.validate()
    assert t.inorder() == list(range(1, 101, 2))
