"""Chapter 21: Mergesort and stable sorting."""


# ==== EX 21.1 | Merge two sorted arrays | Core
# PROMPT: Write `merge(a, b)` returning one sorted list from two sorted lists, using two indices that advance through them. No `sorted()`.
# EXAMPLE: `merge([1, 4, 9], [2, 3, 10, 11])` -> `[1, 2, 3, 4, 9, 10, 11]`
# BIGO: O(N + M) time, O(N + M) space.
# NOTE: Use `<=` when comparing so equal items from `a` come first. That one character is what makes mergesort stable (21.7).
def merge(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 21.2 | Count the comparisons in a merge | Core
# PROMPT: Write `merge_comparisons(a, b)` returning `(merged, comparisons)`. Find inputs that need the fewest and the most comparisons.
# EXAMPLE: `merge_comparisons([1, 2, 3], [4, 5, 6])[1]` -> `3`; `merge_comparisons([1, 3, 5], [2, 4, 6])[1]` -> `5`
# BIGO: Between min(N, M) and N + M - 1 comparisons.
def merge_comparisons(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 21.3 | Mergesort, top-down | Core
# PROMPT: Write `mergesort(arr)` returning a new sorted list: split in half, sort each half recursively, then `merge` them. Base case: length 0 or 1.
# EXAMPLE: `mergesort([38, 27, 43, 3, 9, 82, 10])` -> `[3, 9, 10, 27, 38, 43, 82]`
# BIGO: O(N log N) in every case: log2 N levels of splitting, O(N) merging per level. O(N) extra space.
def mergesort(arr):
    raise NotImplementedError
# ==== END


# ==== EX 21.4 | Mergesort with one shared buffer | Practice
# PROMPT: Write `mergesort_in_place(arr)` that sorts `arr` itself, recursing on index ranges and merging into one auxiliary list allocated once, instead of slicing at every level.
# EXAMPLE: `a = [5, 2, 4, 6, 1, 3]; mergesort_in_place(a)` -> `a` is `[1, 2, 3, 4, 5, 6]`
# BIGO: O(N log N) time, O(N) extra space total instead of fresh slices per call.
def mergesort_in_place(arr):
    raise NotImplementedError
# ==== END


# ==== EX 21.5 | Mergesort, bottom-up | Core
# PROMPT: Write `mergesort_bottom_up(arr)` with no recursion: merge runs of width 1 into width 2, then 4, 8, and so on, until one run covers the list.
# EXAMPLE: `mergesort_bottom_up([5, 1, 4, 2, 8, 0, 2])` -> `[0, 1, 2, 2, 4, 5, 8]`
# BIGO: O(N log N) time, O(N) space, and no call stack at all.
def mergesort_bottom_up(arr):
    raise NotImplementedError
# ==== END


# ==== EX 21.6 | Count inversions while merging | Practice
# PROMPT: An inversion is a pair i < j with arr[i] > arr[j]. Write `count_inversions(arr)` by adding, every time an item from the right half is taken first, the number of items still waiting in the left half.
# EXAMPLE: `count_inversions([2, 4, 1, 3, 5])` -> `3`; a reversed list of 5 -> `10`
# BIGO: O(N log N), versus O(N^2) for checking every pair.
def count_inversions(arr):
    raise NotImplementedError
# ==== END


# ==== EX 21.7 | Stability, with records | Core
# PROMPT: Write `mergesort_by(records, key)` that sorts records by `key(record)` and keeps records with equal keys in their original order. Show that quicksort from Chapter 13 does not promise this.
# EXAMPLE: `mergesort_by([("ann", 3), ("bo", 1), ("cy", 3), ("di", 1)], key=lambda r: r[1])` -> `[('bo', 1), ('di', 1), ('ann', 3), ('cy', 3)]`
# BIGO: O(N log N).
def mergesort_by(records, key):
    raise NotImplementedError
# ==== END


# ==== EX 21.8 | Hybrid: insertion sort for small pieces | Stretch
# PROMPT: Write `hybrid_sort(arr, cutoff=16)`: mergesort that switches to insertion sort when a piece has `cutoff` items or fewer. Benchmark it against plain mergesort in Chapter 22.
# EXAMPLE: `hybrid_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0], cutoff=4)` -> `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
# BIGO: Still O(N log N); insertion sort wins on tiny inputs because its constant factor is small. Python's own Timsort does the same trick.
def hybrid_sort(arr, cutoff=16):
    raise NotImplementedError
# ==== END
