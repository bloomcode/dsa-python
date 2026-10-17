import random
from ch51_binary_search_trees import (build_bst, count_nodes, delete, find_max, find_min, height, inorder, insert,
                                      is_valid_bst, level_order, postorder, preorder, search, tree_sort, TreeNode)


def sample_tree():
    """50 -> (25 -> 10, 33), 75, built by hand so tests don't depend on insert."""
    return TreeNode(50, TreeNode(25, TreeNode(10), TreeNode(33)), TreeNode(75))


def grow(values):
    root = None
    for v in values:
        root = insert(root, v)
    return root


def test_ex_51_1():
    root = sample_tree()
    assert search(root, 33).value == 33 and search(root, 40) is None and search(None, 1) is None


def test_ex_51_2():
    root = grow([50, 25, 75, 10, 33])
    assert root.value == 50 and root.left.value == 25 and root.right.value == 75
    assert root.left.left.value == 10 and root.left.right.value == 33


def test_ex_51_3():
    r = grow([50, 25, 75, 61, 89, 52])
    r = delete(r, 50)
    assert r.value == 52 and inorder(r) == [25, 52, 61, 75, 89]
    r = delete(r, 25)  # leaf
    r = delete(r, 89)
    assert inorder(r) == [52, 61, 75]
    assert inorder(delete(r, 99)) == [52, 61, 75]
    rng = random.Random(1)
    for _ in range(100):
        vals = rng.sample(range(200), 30)
        t = grow(vals)
        for v in rng.sample(vals, 15):
            t = delete(t, v)
            vals.remove(v)
        assert inorder(t) == sorted(vals)


def test_ex_51_4():
    root = sample_tree()
    assert inorder(root) == [10, 25, 33, 50, 75]
    assert preorder(root) == [50, 25, 10, 33, 75]
    assert postorder(root) == [10, 33, 25, 75, 50]
    assert inorder(None) == []


def test_ex_51_5():
    root = sample_tree()
    assert find_min(root) == 10 and find_max(root) == 75 and find_min(None) is None


def test_ex_51_6():
    assert height(grow([50, 25, 75, 10])) == 3 and height(grow([1, 2, 3, 4])) == 4 and height(None) == 0


def test_ex_51_7():
    assert inorder(build_bst([50, 25, 75, 10, 33])) == [10, 25, 33, 50, 75]
    assert build_bst([50, 25, 75, 10, 33]).value == 50
    assert tree_sort([5, 3, 8, 1, 4]) == [1, 3, 4, 5, 8]


def test_ex_51_8():
    assert is_valid_bst(sample_tree())
    assert not is_valid_bst(TreeNode(10, TreeNode(5, None, TreeNode(12)), TreeNode(15)))


def test_ex_51_9():
    assert level_order(sample_tree()) == [[50], [25, 75], [10, 33]]


def test_ex_51_10():
    assert count_nodes(sample_tree()) == 5 and count_nodes(None) == 0
