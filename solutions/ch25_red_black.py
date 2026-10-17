"""Chapter 25: Red-black trees.

A shared black sentinel `NIL` stands in for every empty child, as in most textbook
implementations; it removes many None checks from the fix-up code.
"""
import math

RED, BLACK = "R", "B"


# ==== EX 25.1 | Nodes, the NIL sentinel and rotations | Core | class=RedBlackTree
# PROMPT: Create `RBNode(key, color)` with `left`, `right` and `parent`, a `RedBlackTree` whose empty children all point at one black `NIL` sentinel, and `rotate_left(x)` / `rotate_right(x)` that keep parent links and the root correct.
# EXAMPLE: after a left rotation at x, x's old right child takes x's place and x becomes its left child; in-order order is unchanged
# BIGO: O(1) per rotation: three links change.
# NOTE: A rotation never breaks binary-search order. It only changes the shape, which is all balancing needs.
class RBNode:
    __slots__ = ("key", "color", "left", "right", "parent")

    def __init__(self, key, color, nil=None):
        raise NotImplementedError


class RedBlackTree:
    def __init__(self):
        raise NotImplementedError

    def rotate_left(self, x):
        raise NotImplementedError

    def rotate_right(self, x):
        raise NotImplementedError
# ==== END

    # ==== EX 25.2 | Insert with recolouring and rotations | Core | class=RedBlackTree
    # PROMPT: Add `insert(key)`: do a normal BST insert of a red node, then fix up. While the parent is red: if the uncle is red, recolour parent, uncle and grandparent and move up; otherwise rotate (once or twice) and recolour. Finally paint the root black.
    # EXAMPLE: insert 1..7 in sorted order -> root `2`, height `4` (a plain BST would be 7 tall), and `validate()` passes after every insert
    # BIGO: O(log N): the walk down is O(log N), fix-up recolours up the tree and does at most two rotations.
    def insert(self, key):
        raise NotImplementedError

    def _insert_fixup(self, z):
        raise NotImplementedError
    # ==== END

    # ==== EX 25.3 | Check the red-black rules | Core | class=RedBlackTree
    # PROMPT: Add `validate()` returning the tree's black height, and raising `AssertionError` if the root is red, a red node has a red child, BST order is broken, or two paths have different black counts.
    # EXAMPLE: after any sequence of inserts and deletes, `validate()` returns a positive number instead of raising
    # BIGO: O(N). Write this before insert: it is the test that tells you whether your fix-up works.
    def validate(self):
        raise NotImplementedError
    # ==== END

    # ==== EX 25.4 | Search and in-order walk | Core | class=RedBlackTree
    # PROMPT: Add `contains(key)` and `inorder()` (a list of keys). Both ignore colour entirely: a red-black tree is still a BST.
    # EXAMPLE: after inserting `[5, 2, 8, 1]` -> `contains(8)` is `True`; `inorder()` is `[1, 2, 5, 8]`
    # BIGO: Search O(log N) guaranteed; in-order O(N).
    def contains(self, key):
        raise NotImplementedError

    def inorder(self):
        raise NotImplementedError
    # ==== END

    # ==== EX 25.5 | Height stays logarithmic | Core | class=RedBlackTree
    # PROMPT: Add `height()` and check it never exceeds 2 * log2(N + 1), even after inserting 1..N in sorted order (which makes a plain BST N tall).
    # EXAMPLE: insert 1..1000 in order -> `height()` is at most `19`, while a plain BST would be `1000` tall
    # BIGO: O(N) to measure. The bound follows from the rules: no two reds in a row, and equal black counts on every path.
    def height(self):
        raise NotImplementedError

    def height_bound(self):
        raise NotImplementedError
    # ==== END

    # ==== EX 25.6 | Minimum, maximum and successor | Practice | class=RedBlackTree
    # PROMPT: Add `minimum(node=None)`, `maximum()` and `successor(key)` (the smallest key greater than key, or `None`), using parent links for the successor.
    # EXAMPLE: keys `[20, 10, 30, 25]` -> `minimum()` `10`, `maximum()` `30`, `successor(20)` `25`, `successor(30)` `None`
    # BIGO: O(log N) each.
    def minimum(self, node=None):
        raise NotImplementedError

    def maximum(self):
        raise NotImplementedError

    def _find(self, key):
        raise NotImplementedError

    def successor(self, key):
        raise NotImplementedError
    # ==== END

    # ==== EX 25.8 | Deletion | Stretch | class=RedBlackTree
    # PROMPT: Add `delete(key)`. Splice out the node (or its successor), remember the colour removed, and if a black node was removed run the four-case "double black" fix-up with rotations and recolouring. Return `False` if the key is absent.
    # EXAMPLE: insert 1..100, delete every even key -> `validate()` passes and `inorder()` is the odd keys
    # BIGO: O(log N), with at most three rotations.
    def _transplant(self, u, v):
        raise NotImplementedError

    def delete(self, key):
        raise NotImplementedError

    def _delete_fixup(self, x):
        raise NotImplementedError
    # ==== END


# ==== EX 25.7 | Count the rotations | Practice
# PROMPT: Write `rotations_for(keys)` returning how many rotations a red-black tree performs while inserting keys in order. Compare sorted, reversed and shuffled input.
# EXAMPLE: `rotations_for(range(1000))` -> fewer than 1000 rotations in total (amortized O(1) per insert)
# BIGO: At most 2 rotations per insert; amortized fewer.
def rotations_for(keys):
    raise NotImplementedError
# ==== END
