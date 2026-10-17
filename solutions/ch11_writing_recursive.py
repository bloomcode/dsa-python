"""Chapter 11: Thinking recursively."""


# ==== EX 11.1 | Double every element in place | Core
# PROMPT: Write `double_in_place(arr, index=0)` recursively, modifying the list rather than returning a new one ("repeatedly execute" category).
# EXAMPLE: `[1, 2, 3]` -> `[2, 4, 6]`
# BIGO: O(N).
def double_in_place(arr, index=0):
    raise NotImplementedError
# ==== END


# ==== EX 11.2 | Reverse a string | Core
# PROMPT: Write `reverse(s)` top-down: assume `reverse` already works on everything after the first character.
# EXAMPLE: `'abcde'` -> `'edcba'`
# BIGO: O(N) calls (each slice copies, so O(N^2) characters copied in total).
def reverse(s):
    raise NotImplementedError
# ==== END


# ==== EX 11.3 | Count a character | Core
# PROMPT: Write `count_x(s)` returning how many times `'x'` appears.
# EXAMPLE: `'axbxcxd'` -> `3`
# BIGO: O(N).
def count_x(s):
    raise NotImplementedError
# ==== END


# ==== EX 11.4 | Total characters across strings | Core
# PROMPT: Write `total_chars(strings)` returning the sum of all string lengths.
# EXAMPLE: `['ab', 'c', 'def', 'ghij']` -> `10`
# BIGO: O(N) in the number of strings.
def total_chars(strings):
    raise NotImplementedError
# ==== END


# ==== EX 11.5 | Select the even numbers | Core
# PROMPT: Write `select_evens(nums)` returning a new list of only the even numbers.
# EXAMPLE: `[1, 2, 3, 4, 5, 6]` -> `[2, 4, 6]`
# BIGO: O(N).
def select_evens(nums):
    raise NotImplementedError
# ==== END


# ==== EX 11.6 | Triangular numbers | Core
# PROMPT: Write `triangular(n)` returning 1 + 2 + ... + n recursively.
# EXAMPLE: `triangular(7)` -> `28`
# BIGO: O(N).
def triangular(n):
    raise NotImplementedError
# ==== END


# ==== EX 11.7 | Index of the first x | Core
# PROMPT: Write `index_of_x(s, i=0)` returning the first index of `'x'`, or `-1`.
# EXAMPLE: `'abcdefghijklmnopqrstuvwxyz'` -> `23`
# BIGO: O(N).
def index_of_x(s, i=0):
    raise NotImplementedError
# ==== END


# ==== EX 11.8 | The staircase problem | Practice
# PROMPT: Write `staircase(n)`: how many ways to climb n steps taking 1, 2 or 3 at a time. Think top-down: the last move was 1, 2 or 3 steps.
# EXAMPLE: `staircase(3)` -> `4`; `staircase(5)` -> `13`
# BIGO: About O(3^N) as written. Chapter 12 (12.3) brings it to O(N).
def staircase(n):
    raise NotImplementedError
# ==== END


# ==== EX 11.9 | Anagram generation | Practice
# PROMPT: Write `anagrams(s)` returning every arrangement of the characters. For each anagram of `s[1:]`, insert `s[0]` at every position.
# EXAMPLE: `'abc'` -> `['abc', 'bac', 'bca', 'acb', 'cab', 'cba']` (any order)
# BIGO: O(N!). Six letters already give 720 results.
def anagrams(s):
    raise NotImplementedError
# ==== END


# ==== EX 11.10 | Unique paths through a grid | Practice
# PROMPT: Write `unique_paths(rows, cols)`: moving only right or down, how many paths lead from the top-left to the bottom-right cell?
# EXAMPLE: `unique_paths(3, 7)` -> `28`
# BIGO: Exponential as written. Memoised in 12.4.
def unique_paths(rows, cols):
    raise NotImplementedError
# ==== END


# ==== EX 11.11 | All subsets | Stretch
# PROMPT: Write `subsets(items)` returning every subset (the power set). Each subset of the rest appears once without and once with the first item.
# EXAMPLE: `[1, 2]` -> `[[], [2], [1], [1, 2]]` (any order)
# BIGO: O(2^N) subsets.
def subsets(items):
    raise NotImplementedError
# ==== END
