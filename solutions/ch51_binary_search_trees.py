"""Chapter 51: Binary search trees."""
from collections import deque


# ==== EX 51.1 | Tree node and search | Core
# PROMPT: Create `TreeNode(value, left=None, right=None)`. Write `search(node, value)` returning the node holding `value`, or `None`: go left if smaller, right if larger.
# EXAMPLE: Tree from `[50, 25, 75, 10, 33]` -> `search(root, 33).value` is `33`; `search(root, 40)` is `None`
# BIGO: O(log N) in a balanced tree; O(N) in a degenerate one (sorted inserts make a linked list).
class TreeNode:
    def __init__(self, value, left=None, right=None):
        raise NotImplementedError


def search(node, value):
    raise NotImplementedError
# ==== END


# ==== EX 51.2 | Insert | Core
# PROMPT: Write `insert(node, value)` that returns the (possibly new) root. Walk down as in search; attach a new leaf at the first empty child. Ignore duplicates.
# EXAMPLE: `root = None; for v in [50, 25, 75]: root = insert(root, v)` -> root 50, left 25, right 75
# BIGO: O(log N) balanced, O(N) worst case.
def insert(node, value):
    raise NotImplementedError
# ==== END


# ==== EX 51.3 | Delete (all three cases) | Core
# PROMPT: Write `delete(node, value)` returning the new subtree root. Handle: no children (remove it), one child (the child takes its place), two children (replace the value with its successor, the smallest value in the right subtree, then delete the successor from there).
# EXAMPLE: Deleting 50 from `[50, 25, 75, 61, 89, 52]` makes 52 the new root value
# BIGO: O(log N) balanced.
def delete(node, value):
    raise NotImplementedError
# ==== END


# ==== EX 51.4 | Traversals | Core
# PROMPT: Write `inorder(node)`, `preorder(node)` and `postorder(node)`, each returning a list of values.
# EXAMPLE: Tree from `[50, 25, 75, 10, 33]` -> inorder `[10, 25, 33, 50, 75]`, preorder `[50, 25, 10, 33, 75]`, postorder `[10, 33, 25, 75, 50]`
# BIGO: O(N): every node is visited once.
# NOTE: In-order traversal of a BST always yields sorted values.
def inorder(node):
    raise NotImplementedError


def preorder(node):
    raise NotImplementedError


def postorder(node):
    raise NotImplementedError
# ==== END


# ==== EX 51.5 | Minimum and maximum | Core
# PROMPT: Write `find_min(node)` and `find_max(node)` by walking only left or only right.
# EXAMPLE: Tree from `[50, 25, 75, 10, 33]` -> `10` and `75`
# BIGO: O(log N) balanced (the height of the tree).
def find_min(node):
    raise NotImplementedError


def find_max(node):
    raise NotImplementedError
# ==== END


# ==== EX 51.6 | Height | Core
# PROMPT: Write `height(node)`: the number of nodes on the longest root-to-leaf path (empty tree = 0).
# EXAMPLE: Tree from `[50, 25, 75, 10]` -> `3`; from sorted `[1, 2, 3, 4]` -> `4`
# BIGO: O(N). Compare log2(N) to the height to see how balanced a tree is.
def height(node):
    raise NotImplementedError
# ==== END


# ==== EX 51.7 | Build a tree and tree-sort | Practice
# PROMPT: Write `build_bst(values)` returning the root, and `tree_sort(values)` = build, then in-order. Try sorted input and see `height`.
# EXAMPLE: `tree_sort([5, 3, 8, 1, 4])` -> `[1, 3, 4, 5, 8]`
# BIGO: O(N log N) on random input, O(N^2) on sorted input (the tree degenerates).
def build_bst(values):
    raise NotImplementedError


def tree_sort(values):
    raise NotImplementedError
# ==== END


# ==== EX 51.8 | Validate a BST | Practice
# PROMPT: Write `is_valid_bst(node)`. Checking only each node's direct children is not enough: pass down the allowed `(low, high)` range.
# EXAMPLE: `TreeNode(10, TreeNode(5, None, TreeNode(12)), TreeNode(15))` -> `False` (12 sits left of 10)
# BIGO: O(N).
def is_valid_bst(node, low=float("-inf"), high=float("inf")):
    raise NotImplementedError
# ==== END


# ==== EX 51.9 | Level-order traversal | Practice
# PROMPT: Write `level_order(node)` returning a list of levels (each a list of values), using a queue.
# EXAMPLE: Tree from `[50, 25, 75, 10, 33]` -> `[[50], [25, 75], [10, 33]]`
# BIGO: O(N) time, O(W) space for the widest level.
def level_order(node):
    raise NotImplementedError
# ==== END


# ==== EX 51.10 | Count the nodes | Core
# PROMPT: Write `count_nodes(node)` recursively.
# EXAMPLE: Tree from `[50, 25, 75, 10, 33]` -> `5`
# BIGO: O(N).
def count_nodes(node):
    raise NotImplementedError
# ==== END
