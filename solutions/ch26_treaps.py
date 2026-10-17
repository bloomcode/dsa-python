"""Chapter 26: Treaps: balance from random priorities.

A treap is a BST by key and a heap by a random priority (here: a max-heap, so a
parent's priority is at least its children's). Functions take a node and return the
new subtree root, like the BST code in Chapter 15.
"""


# ==== EX 26.1 | Treap nodes and rotations | Core
# PROMPT: Create `TreapNode(key, priority)` with `left` and `right`, and write `rotate_right(node)` and `rotate_left(node)` that return the new subtree root.
# EXAMPLE: rotating right at a node with left child L makes L the subtree root and the old node L's right child
# BIGO: O(1).
class TreapNode:
    __slots__ = ("key", "priority", "left", "right")

    def __init__(self, key, priority):
        raise NotImplementedError


def rotate_right(node):
    raise NotImplementedError


def rotate_left(node):
    raise NotImplementedError
# ==== END


# ==== EX 26.2 | Insert, then rotate up | Core
# PROMPT: Write `treap_insert(node, key, rng)` that gives the new key `rng.random()` as its priority, inserts it as a BST leaf, and on the way back up rotates it above any parent with a smaller priority.
# EXAMPLE: `rng = random.Random(1); root = None; for k in range(10): root = treap_insert(root, k, rng)` -> a valid treap whose in-order walk is 0..9
# BIGO: O(log N) expected, whatever order the keys arrive in.
def treap_insert(node, key, rng, priority=None):
    raise NotImplementedError
# ==== END


# ==== EX 26.3 | Search | Core
# PROMPT: Write `treap_contains(node, key)`. Priorities play no part in search.
# EXAMPLE: after inserting `[5, 2, 8]` -> `treap_contains(root, 8)` is `True`, `treap_contains(root, 3)` is `False`
# BIGO: O(log N) expected.
def treap_contains(node, key):
    raise NotImplementedError
# ==== END


# ==== EX 26.4 | Delete by rotating down | Core
# PROMPT: Write `treap_delete(node, key)`: find the node, then rotate it down (always lifting the child with the larger priority) until it has at most one child, and splice it out.
# EXAMPLE: insert 0..99, delete the multiples of 3 -> in-order gives the other 66 keys and the treap is still valid
# BIGO: O(log N) expected.
def treap_delete(node, key):
    raise NotImplementedError
# ==== END


# ==== EX 26.5 | Validate both orders at once | Core
# PROMPT: Write `is_valid_treap(node)` checking BST order on keys and heap order on priorities in one recursive pass, and `inorder(node)`.
# EXAMPLE: any treap built by 26.2 -> `True`; swap two priorities by hand -> `False`
# BIGO: O(N).
def is_valid_treap(node, lo=None, hi=None):
    raise NotImplementedError


def inorder(node):
    raise NotImplementedError
# ==== END


# ==== EX 26.6 | Random priorities do the balancing | Core
# PROMPT: Write `treap_height(keys, rng)` building a treap from keys inserted in the given order. Insert 1..1000 in sorted order and compare with a plain BST (23.6).
# EXAMPLE: sorted 1..1000 with `random.Random(0)` -> height around 20 to 30, versus 1000 for a plain BST
# BIGO: Expected height about 3 x log2 N, the same as a BST built from shuffled keys, so roughly 25 to 30 for N = 1000.
def treap_height(keys, rng):
    raise NotImplementedError
# ==== END


# ==== EX 26.7 | Split and merge | Stretch
# PROMPT: Write `split(node, key)` returning `(left, right)` treaps with keys < key and >= key, and `merge(a, b)` joining treaps where every key in a is smaller than every key in b. Use them to delete a whole key range.
# EXAMPLE: split a treap of 0..9 at 4 -> in-orders `[0, 1, 2, 3]` and `[4, 5, 6, 7, 8, 9]`; merging them restores 0..9
# BIGO: O(log N) expected each. Many contest "implicit treap" tricks are built from these two operations.
def split(node, key):
    raise NotImplementedError


def merge(a, b):
    raise NotImplementedError
# ==== END
