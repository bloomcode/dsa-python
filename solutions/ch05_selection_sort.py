"""Chapter 5: Selection sort and constant factors."""


# ==== EX 5.1 | Selection sort | Core
# PROMPT: Write `selection_sort(arr)`: on each pass find the index of the smallest unsorted value and swap it into place (one swap per pass at most).
# EXAMPLE: `[4, 2, 7, 1, 3]` -> `[1, 2, 3, 4, 7]`
# BIGO: O(N^2) time, O(1) space. About N^2/2 comparisons but at most N - 1 swaps.
def selection_sort(arr):
    raise NotImplementedError
# ==== END


# ==== EX 5.2 | Bubble vs selection: count the work | Practice
# PROMPT: Write `bubble_counts(arr)` and `selection_counts(arr)`, each sorting a copy and returning `(comparisons, swaps)`. Compare them on a reversed list of 10.
# EXAMPLE: Reversed 10 elements -> bubble `(45, 45)`, selection `(45, 5)`
# BIGO: Both O(N^2). Selection does roughly half the total steps; Big O ignores that constant, which is why both share a category.
def bubble_counts(arr):
    raise NotImplementedError


def selection_counts(arr):
    raise NotImplementedError
# ==== END


# ==== EX 5.3 | Every other element | Core
# PROMPT: Write `every_other(arr)` returning elements at indices 0, 2, 4 and so on, using a loop that steps by 2.
# EXAMPLE: `[10, 11, 12, 13, 14]` -> `[10, 12, 14]`
# BIGO: N/2 steps, which is still O(N): constants are dropped.
def every_other(arr):
    raise NotImplementedError
# ==== END


# ==== EX 5.4 | Second largest in one pass | Practice
# PROMPT: Write `second_largest(arr)` returning the second-largest distinct value, or `None`, in a single pass and without sorting.
# EXAMPLE: `[5, 1, 9, 7, 9]` -> `7`; `[3, 3]` -> `None`
# BIGO: O(N) time, O(1) space. Sorting first would be O(N log N).
def second_largest(arr):
    raise NotImplementedError
# ==== END


# ==== EX 5.5 | K smallest by partial selection sort | Stretch
# PROMPT: Write `k_smallest(arr, k)` that runs only the first `k` passes of selection sort on a copy and returns the first `k` values.
# EXAMPLE: `[8, 3, 5, 1, 9]`, k = 2 -> `[1, 3]`
# BIGO: O(kN). Better than a full O(N^2) sort when k is small.
def k_smallest(arr, k):
    raise NotImplementedError
# ==== END
