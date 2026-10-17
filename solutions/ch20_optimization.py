"""Chapter 20: Making code faster: lookups, patterns and greed."""


# ==== EX 20.1 | Two sum with a magical lookup | Core
# PROMPT: Write `has_two_sum(nums, target)` returning `True` if any two numbers add to `target`. Ask: "if I could look up any value in O(1), what would I look for?"
# EXAMPLE: `[2, 0, 4, 1, 7, 9]`, 10 -> `True` (1 + 9)
# BIGO: O(N) time, O(N) space; the brute force is O(N^2).
def has_two_sum(nums, target):
    raise NotImplementedError
# ==== END


# ==== EX 20.2 | Sum swap | Practice
# PROMPT: Write `sum_swap(a, b)` returning indices `(i, j)` such that swapping `a[i]` and `b[j]` makes the two sums equal, or `None`. Spot the pattern: the swap must shift each sum by half the difference.
# EXAMPLE: `[5, 3, 2, 9, 1]` (sum 20), `[1, 12, 5]` (sum 18) -> `(2, 0)`: swapping 2 and 1 gives 19 and 19
# BIGO: O(N + M) with a hash table of one list's values.
def sum_swap(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 20.3 | Greatest subarray sum (greedy) | Core
# PROMPT: Write `max_subarray_sum(nums)` in one pass: keep a running sum, reset it to 0 when it goes negative, and track the best seen.
# EXAMPLE: `[3, -4, 4, -3, 5, -9]` -> `6` (4 - 3 + 5)
# BIGO: O(N) time, O(1) space (Kadane's algorithm), versus O(N^2) for every subarray.
# NOTE: Initialise `best` with the first value, not 0, so an all-negative list returns its largest value.
def max_subarray_sum(nums):
    raise NotImplementedError
# ==== END


# ==== EX 20.4 | Increasing triplet (greedy) | Practice
# PROMPT: Write `has_increasing_triplet(nums)`: are there i < j < k with nums[i] < nums[j] < nums[k]? Track the lowest value and a "middle" value in one pass.
# EXAMPLE: `[22, 25, 21, 18, 19.6, 17, 16, 20.5]` -> `True` (18, 19.6, 20.5); `[5, 4, 3]` -> `False`
# BIGO: O(N) time, O(1) space.
def has_increasing_triplet(nums):
    raise NotImplementedError
# ==== END


# ==== EX 20.5 | Best stock trade | Core
# PROMPT: Write `max_profit(prices)`: the most money from buying once and selling later (0 if prices only fall).
# EXAMPLE: `[10, 7, 5, 8, 11, 2, 6]` -> `6` (buy 5, sell 11)
# BIGO: O(N) greedy, one pass tracking the lowest price so far.
def max_profit(prices):
    raise NotImplementedError
# ==== END


# ==== EX 20.6 | Anagram check by changing the data structure | Core
# PROMPT: Write `are_anagrams(a, b)` by counting characters in a dict, instead of generating permutations (11.9) or sorting.
# EXAMPLE: `'listen'`, `'silent'` -> `True`
# BIGO: O(N + M). Sorting is O(N log N); generating anagrams is O(N!).
def are_anagrams(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 20.7 | Sort values from a small known range | Practice
# PROMPT: Body temperatures are recorded to one decimal place between 97.0 and 99.0. Write `sort_temperatures(temps)` in O(N) by counting how many of each reading occur, then emitting them in order.
# EXAMPLE: `[98.6, 98.0, 97.1, 99.0, 98.9, 97.8, 98.5, 98.2, 98.0, 97.1]` -> `[97.1, 97.1, 97.8, 98.0, 98.0, 98.2, 98.5, 98.6, 98.9, 99.0]`
# BIGO: O(N + R) where R = 21 possible readings, so O(N). A known small range beats O(N log N) sorting.
def sort_temperatures(temps):
    raise NotImplementedError
# ==== END


# ==== EX 20.8 | Missing number in O(N) | Core
# PROMPT: Revisit 13.6. Write `missing_number(arr)` using the formula for 0 + 1 + ... + n = n(n + 1) / 2.
# EXAMPLE: `[5, 2, 4, 1, 0]` -> `3`
# BIGO: O(N) time, O(1) space, versus O(N log N) by sorting.
def missing_number(arr):
    raise NotImplementedError
# ==== END


# ==== EX 20.9 | Longest consecutive run | Stretch
# PROMPT: Write `longest_consecutive(nums)` returning the length of the longest run of consecutive integers in an unsorted list, in O(N). Only start counting from a number whose predecessor is absent.
# EXAMPLE: `[10, 5, 12, 3, 55, 30, 4, 11, 2]` -> `4` (2, 3, 4, 5)
# BIGO: O(N): each number is visited at most twice across all runs.
def longest_consecutive(nums):
    raise NotImplementedError
# ==== END
