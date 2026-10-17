"""Chapter 73: Greedy choices and problem transforms."""


# ==== EX 73.1 | Pair with a given difference | Core
# PROMPT: Write `has_pair_with_difference(nums, d)` for `d >= 0`: is there a pair of positions whose values differ by exactly `d`? Keep a set of values seen so far and check `x + d` and `x - d` before adding `x`.
# EXAMPLE: `[1, 8, 4, 11], 3` -> `True`; `[1, 5], 3` -> `False`
# BIGO: O(N): one pass with O(1) set lookups, instead of O(N^2) for every pair.
def has_pair_with_difference(nums, d):
    raise NotImplementedError
# ==== END


# ==== EX 73.2 | Window with a target sum | Practice
# PROMPT: For a list of non-negative numbers, write `window_with_sum(nums, target)` returning `(i, j)` for the first run `nums[i..j]` (inclusive) that adds up to `target`, or `None`. Slide a window: grow it on the right, and shrink it from the left while its sum is too big.
# EXAMPLE: `[2, 4, 3, 5, 1], 8` -> `(2, 3)`; `[1, 2], 7` -> `None`
# BIGO: O(N): each index enters the window once and leaves it at most once.
def window_with_sum(nums, target):
    raise NotImplementedError
# ==== END


# ==== EX 73.3 | Can you reach the end? | Core
# PROMPT: From index `i` you may jump forward up to `jumps[i]` places. Write `can_reach_end(jumps)` for a non-empty list: can you get from index 0 to the last index? Track the furthest index you could reach; if you ever stand beyond it, you are stuck.
# EXAMPLE: `[2, 3, 1, 1, 4]` -> `True`; `[3, 2, 1, 0, 4]` -> `False`
# BIGO: O(N): one pass keeping the furthest index reachable so far.
def can_reach_end(jumps):
    raise NotImplementedError
# ==== END


# ==== EX 73.4 | Rooms needed for meetings | Practice
# PROMPT: Write `rooms_needed(meetings)` for `[start, end]` pairs: the fewest rooms so no two meetings in one room overlap (a room is free again at its meeting's end time). Sort the starts and the ends separately and sweep through the starts.
# EXAMPLE: `[[9, 11], [10, 12], [11, 13], [9, 10]]` -> `2`
# BIGO: O(N log N) for the two sorts, then one linear sweep.
# NOTE: Sorting starts and ends separately loses which end belongs to which meeting, and that is fine: the count of rooms only depends on how many meetings are running at once.
def rooms_needed(meetings):
    raise NotImplementedError
# ==== END


# ==== EX 73.5 | Most meetings in one room | Core
# PROMPT: Write `max_meetings(meetings)` for `[start, end]` pairs: the largest number that fit in one room without overlapping (one may start when another ends). Sort by end time and keep each meeting that starts no earlier than the last one kept ends.
# EXAMPLE: `[[1, 4], [3, 5], [0, 6], [5, 7], [8, 9], [5, 9]]` -> `3`
# BIGO: O(N log N): sort by end time, then one greedy pass.
# NOTE: Taking the meeting that ends first always leaves the most time for the rest; taking the shortest, or the earliest to start, does not.
def max_meetings(meetings):
    raise NotImplementedError
# ==== END


# ==== EX 73.6 | Range totals after one pass | Core | class=RangeSum
# PROMPT: Build `RangeSum(nums)` that precomputes running totals so `total(i, j)` returns `nums[i] + ... + nums[j]` (inclusive) without a loop.
# EXAMPLE: `RangeSum([3, 1, 4, 1, 5]).total(1, 3)` -> `6`
# BIGO: O(N) once to build, then O(1) per query instead of O(N) per query.
class RangeSum:
    def __init__(self, nums):
        raise NotImplementedError

    def total(self, i, j):
        raise NotImplementedError
# ==== END


# ==== EX 73.7 | Most frequent words with buckets | Practice
# PROMPT: Write `top_k_frequent(words, k)` returning the `k` most frequent words, most frequent first; words with equal counts keep the order in which they first appeared. Put each word into bucket number `count` and read the buckets from the top.
# EXAMPLE: `['b', 'a', 'b', 'c', 'a', 'b'], 2` -> `['b', 'a']`
# BIGO: O(N): count once, then drop each word into a bucket indexed by its count instead of sorting.
def top_k_frequent(words, k):
    raise NotImplementedError
# ==== END


# ==== EX 73.8 | The value without a partner | Core
# PROMPT: Every value in `nums` appears exactly twice except one. Write `lone_value(nums)` returning it in one pass with no extra memory, by combining everything with XOR (`^`).
# EXAMPLE: `[4, 1, 2, 1, 2]` -> `4`
# BIGO: O(N) time, O(1) space: `x ^ x` is 0 and `x ^ 0` is x, so every pair cancels out.
def lone_value(nums):
    raise NotImplementedError
# ==== END


# ==== EX 73.9 | Longest stretch without a repeat | Stretch
# PROMPT: Write `longest_unique_run(s)` returning the length of the longest stretch of consecutive characters with no character repeated. Slide a window and remember where each character was last seen; on a repeat inside the window, move the start just past that earlier position.
# EXAMPLE: `'abcadbe'` -> `5`; `'aaaa'` -> `1`
# BIGO: O(N): each index enters the window once, and a table of last positions moves the start forward in one jump.
def longest_unique_run(s):
    raise NotImplementedError
# ==== END
