"""Chapter 13: Partitioning: quicksort and quickselect."""


# ==== EX 13.1 | Partition | Core
# PROMPT: Write `partition(arr, left, right)` using the rightmost element as pivot: a left pointer moves right past values smaller than the pivot, a right pointer moves left past values larger, swap, repeat; finally swap the pivot into the left pointer's spot. Return the pivot's final index.
# EXAMPLE: `[0, 5, 2, 1, 6, 3]` -> pivot 3 ends at index 3, values left of it are all < 3, right of it all > 3
# BIGO: O(N) for one partition.
def partition(arr, left, right):
    raise NotImplementedError
# ==== END


# ==== EX 13.2 | Quicksort | Core
# PROMPT: Write `quicksort(arr, left=0, right=None)`: partition, then recurse on the sub-arrays left and right of the pivot. Base case: fewer than two elements.
# EXAMPLE: `[0, 5, 2, 1, 6, 3]` -> `[0, 1, 2, 3, 5, 6]`
# BIGO: O(N log N) average, O(N^2) worst case (pivot is always the smallest or largest, e.g. sorted input with a rightmost pivot).
def quicksort(arr, left=0, right=None):
    raise NotImplementedError
# ==== END


# ==== EX 13.3 | Quickselect | Core
# PROMPT: Write `quickselect(arr, k)` returning the k-th smallest value (k = 0 is the minimum) without fully sorting: partition, then recurse into only the side that holds index k.
# EXAMPLE: `[0, 50, 20, 10, 60, 30]`, k = 1 -> `10`
# BIGO: O(N) average (N + N/2 + N/4 ... = 2N), O(N^2) worst case.
def quickselect(arr, k, left=0, right=None):
    raise NotImplementedError
# ==== END


# ==== EX 13.4 | Duplicates via sorting | Core
# PROMPT: Write `has_duplicates_sorted(arr)`: sort a copy with your quicksort, then compare neighbours.
# EXAMPLE: `[5, 9, 3, 2, 4, 5, 6]` -> `True`
# BIGO: O(N log N) time. It sits between the O(N^2) nested loops of 4.3 and the O(N)-space set of 4.4; sorting the input in place instead of a copy would cut extra space to quicksort's O(log N) call stack.
def has_duplicates_sorted(arr):
    raise NotImplementedError
# ==== END


# ==== EX 13.5 | Greatest product of three | Practice
# PROMPT: Write `max_product_of_three(nums)`. Sort first; remember two large negatives can make a large positive.
# EXAMPLE: `[1, 10, 2, 6, 5, 3]` -> `300`; `[-10, -10, 1, 3, 2]` -> `300`
# BIGO: O(N log N).
def max_product_of_three(nums):
    raise NotImplementedError
# ==== END


# ==== EX 13.6 | Missing number via sorting | Core
# PROMPT: A list holds every integer 0..n except one. Write `missing_number_sorted(arr)` by sorting and finding where index and value disagree.
# EXAMPLE: `[5, 2, 4, 1, 0]` -> `3`; `[0, 1, 2]` -> `3`
# BIGO: O(N log N). Chapter 20 (20.8) gets it to O(N).
def missing_number_sorted(arr):
    raise NotImplementedError
# ==== END


# ==== EX 13.7 | Median with quickselect | Practice
# PROMPT: Write `median(nums)` using `quickselect`. For an even count, average the two middle values.
# EXAMPLE: `[7, 1, 3]` -> `3`; `[4, 1, 3, 2]` -> `2.5`
# BIGO: O(N) average.
def median(nums):
    raise NotImplementedError
# ==== END


# ==== EX 13.8 | Merge sort for comparison | Stretch
# PROMPT: Write `merge_sort(arr)` returning a new sorted list: split in half, sort each half recursively, merge (reuse 6.5's idea).
# EXAMPLE: `[38, 27, 43, 3, 9, 82, 10]` -> `[3, 9, 10, 27, 38, 43, 82]`
# BIGO: O(N log N) in every case, but O(N) extra space, unlike quicksort's in-place partitioning.
def merge_sort(arr):
    raise NotImplementedError
# ==== END
