"""Chapter 6: Insertion sort in the best and worst case."""


# ==== EX 6.1 | Insertion sort | Core
# PROMPT: Write `insertion_sort(arr)`: for each index from 1, lift the value out ("temp"), shift larger values on its left one slot right, and drop the value into the gap.
# EXAMPLE: `[4, 2, 7, 1, 3]` -> `[1, 2, 3, 4, 7]`
# BIGO: Worst O(N^2), average about N^2/2, best (already sorted) O(N). O(1) space.
def insertion_sort(arr):
    raise NotImplementedError
# ==== END


# ==== EX 6.2 | Best, average, worst case in numbers | Practice
# PROMPT: Write `insertion_sort_steps(arr)` that sorts a copy and returns the count of comparisons plus shifts. Run it on a sorted, a random, and a reversed list of 100.
# EXAMPLE: Sorted 100 -> `99`; reversed 100 -> `9900`; random lands in between
# BIGO: Shows O(N) best case and O(N^2) worst case for the same algorithm.
# NOTE: When data is usually nearly sorted, insertion sort can beat selection sort, despite sharing O(N^2).
def insertion_sort_steps(arr):
    raise NotImplementedError
# ==== END


# ==== EX 6.3 | Intersection of two arrays with early break | Core
# PROMPT: Write `intersection_nested(a, b)` returning values in both lists, using nested loops that `break` once a match is found.
# EXAMPLE: `[3, 1, 4, 2]`, `[4, 5, 3, 6]` -> `[3, 4]`
# BIGO: O(N * M) worst case. The `break` only improves the average case.
def intersection_nested(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 6.4 | Insert one value into a sorted array | Core
# PROMPT: Write `insert_sorted(arr, value)` that performs a single insertion-sort step: append, then shift left until the value is in place.
# EXAMPLE: `[1, 4, 9]`, value `5` -> `[1, 4, 5, 9]`
# BIGO: O(N) worst case, O(1) if the value belongs at the end.
def insert_sorted(arr, value):
    raise NotImplementedError
# ==== END


# ==== EX 6.5 | Merge two sorted arrays | Practice
# PROMPT: Write `merge_sorted(a, b)` returning one sorted list using two pointers. No `sorted()`.
# EXAMPLE: `[1, 4, 7]`, `[2, 3, 9]` -> `[1, 2, 3, 4, 7, 9]`
# BIGO: O(N + M) time, O(N + M) space.
def merge_sorted(a, b):
    raise NotImplementedError
# ==== END
