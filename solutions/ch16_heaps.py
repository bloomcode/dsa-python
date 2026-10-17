"""Chapter 16: Heaps and priority queues."""
import heapq
import itertools


# ==== EX 16.1 | Array-backed max-heap skeleton | Core | class=MaxHeap
# PROMPT: Create `MaxHeap` storing nodes in a list `data`. Add `root()`, `last()`, `__len__`, and static helpers `left_child(i)`, `right_child(i)`, `parent(i)`.
# EXAMPLE: `left_child(0)` -> `1`, `right_child(0)` -> `2`, `parent(4)` -> `1`
# BIGO: All O(1). Storing the heap in an array solves "find the last node" for free: it is the last element.
# NOTE: For index i: left child 2i + 1, right child 2i + 2, parent (i - 1) // 2.
class MaxHeap:
    def __init__(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def root(self):
        raise NotImplementedError

    def last(self):
        raise NotImplementedError

    @staticmethod
    def left_child(i):
        raise NotImplementedError

    @staticmethod
    def right_child(i):
        raise NotImplementedError

    @staticmethod
    def parent(i):
        raise NotImplementedError
# ==== END

    # ==== EX 16.2 | Insert and trickle up | Core | class=MaxHeap
    # PROMPT: Add `insert(value)`: append it as the new last node, then swap it with its parent while it is larger than the parent.
    # EXAMPLE: insert 3, 9, 5, 12 -> `root()` is `12`
    # BIGO: O(log N): at most one swap per level of the tree.
    def insert(self, value):
        raise NotImplementedError
    # ==== END

    # ==== EX 16.3 | Delete the root and trickle down | Core | class=MaxHeap
    # PROMPT: Add `delete()` returning the root: move the last node into the root, then swap it with its larger child while a child is larger.
    # EXAMPLE: After inserting 3, 9, 5, 12 -> `delete()` returns 12, 9, 5, 3 in that order
    # BIGO: O(log N).
    # NOTE: Always swap with the larger child; swapping with the smaller one would put a smaller value above a larger one.
    def delete(self):
        raise NotImplementedError
    # ==== END


# ==== EX 16.4 | Heap sort with your heap | Practice
# PROMPT: Write `heap_sort(values)`: insert everything into a `MaxHeap`, delete repeatedly, reverse.
# EXAMPLE: `[5, 1, 9, 3, 7]` -> `[1, 3, 5, 7, 9]`
# BIGO: O(N log N) time, O(N) space as written.
def heap_sort(values):
    raise NotImplementedError
# ==== END


# ==== EX 16.5 | Emergency-room priority queue | Core | class=TriageQueue
# PROMPT: Build `TriageQueue` with `admit(name, severity)` and `next_patient()`, serving the highest severity first and, on a tie, whoever arrived first. Use `heapq` (a min-heap) by pushing `(-severity, arrival_number, name)`.
# EXAMPLE: admit ('Ann', 3), ('Bo', 9), ('Cy', 9) -> next is 'Bo', then 'Cy', then 'Ann'
# BIGO: O(log N) per admit and per next_patient. An ordered array would be O(N) to admit.
class TriageQueue:
    def __init__(self):
        raise NotImplementedError

    def admit(self, name, severity):
        raise NotImplementedError

    def next_patient(self):
        raise NotImplementedError
# ==== END


# ==== EX 16.6 | Top K largest | Practice
# PROMPT: Write `top_k(nums, k)` keeping a min-heap of size k: push each number, pop when the heap grows past k. Return the k largest, largest first.
# EXAMPLE: `[3, 1, 9, 7, 5, 8]`, k = 3 -> `[9, 8, 7]`
# BIGO: O(N log K) time, O(K) space. Better than sorting when K is much smaller than N.
def top_k(nums, k):
    raise NotImplementedError
# ==== END


# ==== EX 16.7 | Is this array a max-heap? | Core
# PROMPT: Write `is_max_heap(arr)` checking that every parent is at least as large as its children, using the index formulas.
# EXAMPLE: `[100, 88, 25, 87, 16]` -> `True`; `[10, 20]` -> `False`
# BIGO: O(N).
def is_max_heap(arr):
    raise NotImplementedError
# ==== END


# ==== EX 16.8 | Merge K sorted lists | Stretch
# PROMPT: Write `merge_k_sorted(lists)` using a heap holding one `(value, list_index, element_index)` entry per list.
# EXAMPLE: `[[1, 4, 7], [2, 5], [0, 9]]` -> `[0, 1, 2, 4, 5, 7, 9]`
# BIGO: O(N log K) for N total values across K lists.
def merge_k_sorted(lists):
    raise NotImplementedError
# ==== END
