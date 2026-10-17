import random

from ch26_treaps import (TreapNode, inorder, is_valid_treap, merge, rotate_left, rotate_right, split, treap_contains,
                         treap_delete, treap_height, treap_insert)


def treap(keys, rng):
    root = None
    for k in keys:
        root = treap_insert(root, k, rng)
    return root


def keys_of(node):
    return [] if node is None else keys_of(node.left) + [node.key] + keys_of(node.right)


def test_ex_26_1():
    top, left, a, b, c = TreapNode(5, 0.5), TreapNode(3, 0.9), TreapNode(1, 0.1), TreapNode(4, 0.2), TreapNode(7, 0.3)
    top.left, top.right, left.left, left.right = left, c, a, b
    root = rotate_right(top)
    assert root is left and root.right is top and top.left is b and keys_of(root) == [1, 3, 4, 5, 7]
    root = rotate_left(root)
    assert root is top and top.left is left and left.right is b and keys_of(root) == [1, 3, 4, 5, 7]


def test_ex_26_2():
    root = treap(range(10), random.Random(1))
    assert keys_of(root) == list(range(10))
    stack = [root]
    while stack:
        n = stack.pop()
        for child in (n.left, n.right):
            if child:
                assert child.priority <= n.priority
                stack.append(child)


def test_ex_26_3():
    root = None
    for k in [5, 2, 8]:
        root = treap_insert(root, k, random.Random(k))
    assert treap_contains(root, 8) and not treap_contains(root, 3) and not treap_contains(None, 1)


def test_ex_26_4():
    root = treap(range(100), random.Random(2))
    for k in range(0, 100, 3):
        root = treap_delete(root, k)
    assert keys_of(root) == [k for k in range(100) if k % 3]
    assert keys_of(treap_delete(root, 1000)) == [k for k in range(100) if k % 3]


def test_ex_26_5():
    root = treap(range(10), random.Random(1))
    assert inorder(root) == list(range(10)) and is_valid_treap(root)
    bad = TreapNode(5, 0.1)
    bad.left = TreapNode(2, 0.9)
    assert not is_valid_treap(bad)
    unordered = TreapNode(5, 0.9)
    unordered.left = TreapNode(7, 0.1)
    assert not is_valid_treap(unordered)


def test_ex_26_6():
    assert treap_height(range(1, 1001), random.Random(0)) < 40


def test_ex_26_7():
    root = treap(range(10), random.Random(5))
    a, b = split(root, 4)
    assert keys_of(a) == [0, 1, 2, 3] and keys_of(b) == [4, 5, 6, 7, 8, 9]
    assert is_valid_treap(a) and is_valid_treap(b)
    m = merge(a, b)
    assert keys_of(m) == list(range(10)) and is_valid_treap(m)
