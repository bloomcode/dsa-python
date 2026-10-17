"""Chapter 4: Bubble sort and quadratic code."""


# ==== EX 4.1 | Bubble sort | Core
# PROMPT: Write `bubble_sort(arr)` that sorts in place by repeatedly comparing neighbours and swapping them when out of order. Return the list.
# EXAMPLE: `[4, 2, 7, 1, 3]` -> `[1, 2, 3, 4, 7]`
# BIGO: O(N^2) time, O(1) space. About N^2/2 comparisons plus up to N^2/2 swaps.
def bubble_sort(arr):
    raise NotImplementedError
# ==== END


# ==== EX 4.2 | Bubble sort with early exit | Practice
# PROMPT: Write `bubble_sort_optimized(arr)` that shrinks the unsorted range each pass and stops as soon as a pass makes no swaps. Return `(arr, passes)`.
# EXAMPLE: `[1, 2, 3, 4]` -> `([1, 2, 3, 4], 1)`; `[4, 3, 2, 1]` -> 3 passes
# BIGO: Worst case still O(N^2); best case (already sorted) O(N).
# NOTE: The largest unsorted value "bubbles" to its final spot each pass, which is why the range can shrink.
def bubble_sort_optimized(arr):
    raise NotImplementedError
# ==== END


# ==== EX 4.3 | Duplicate check, quadratic | Core
# PROMPT: Write `has_duplicate_quadratic(arr)` with two nested loops comparing every pair.
# EXAMPLE: `[1, 5, 3, 9, 1, 4]` -> `True`; `[1, 2, 3]` -> `False`
# BIGO: O(N^2) time, O(1) space.
def has_duplicate_quadratic(arr):
    raise NotImplementedError
# ==== END


# ==== EX 4.4 | Duplicate check, linear | Core
# PROMPT: Write `has_duplicate_linear(arr)` using one loop and a record of values already seen.
# EXAMPLE: Same results as 4.3
# BIGO: O(N) time, O(N) space. Trading memory for speed.
def has_duplicate_linear(arr):
    raise NotImplementedError
# ==== END


# ==== EX 4.5 | Greatest number, two ways | Practice
# PROMPT: Write `greatest_quadratic(arr)` (a value is greatest if no other value beats it, checked with nested loops) and `greatest_linear(arr)` (one pass tracking the best so far).
# EXAMPLE: `[3, 9, 2, 7]` -> `9`
# BIGO: O(N^2) versus O(N), for the same answer.
def greatest_quadratic(arr):
    raise NotImplementedError


def greatest_linear(arr):
    raise NotImplementedError
# ==== END


# ==== EX 4.6 | Is it sorted? | Core
# PROMPT: Write `is_sorted(arr)` that checks ascending order in one pass.
# EXAMPLE: `[1, 2, 2, 5]` -> `True`; `[1, 3, 2]` -> `False`
# BIGO: O(N) worst case, can stop at the first out-of-order pair.
def is_sorted(arr):
    raise NotImplementedError
# ==== END
