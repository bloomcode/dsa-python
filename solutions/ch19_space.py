"""Chapter 19: Counting memory: space complexity."""
import sys


# ==== EX 19.1 | Uppercase: new array vs in place | Core
# PROMPT: Write `uppercase_copy(words)` returning a new list and `uppercase_in_place(words)` modifying the original. State the space complexity of each.
# EXAMPLE: `['amy', 'bob']` -> `['AMY', 'BOB']` either way
# BIGO: Both O(N) time. Copy is O(N) extra space; in place is O(1) extra space.
def uppercase_copy(words):
    raise NotImplementedError


def uppercase_in_place(words):
    raise NotImplementedError
# ==== END


# ==== EX 19.2 | Duplicates: three time/space trade-offs | Core
# PROMPT: Implement three duplicate checks and fill in a time/space table: nested loops (`dup_nested`), a set (`dup_set`), and sort-in-place (`dup_sort_in_place`, which reorders the input).
# EXAMPLE: All three: `[3, 1, 4, 1]` -> `True`
# BIGO: Nested: O(N^2) time, O(1) space. Set: O(N) time, O(N) space. Sort in place: O(N log N) time and no new list of your own, though Python's Timsort may borrow up to N/2 temporary slots. Choose by which resource is scarcer.
def dup_nested(arr):
    raise NotImplementedError


def dup_set(arr):
    raise NotImplementedError


def dup_sort_in_place(arr):
    raise NotImplementedError
# ==== END


# ==== EX 19.3 | The hidden cost of recursion | Core
# PROMPT: Write `sum_to_recursive(n)` and `sum_to_iterative(n)`. Call both with n = 50,000 and catch the `RecursionError` from the recursive one; check `sys.getrecursionlimit()`.
# EXAMPLE: `sum_to_iterative(50_000)` -> `1250025000`; the recursive one raises `RecursionError` (default limit is 1,000)
# BIGO: Both O(N) time. Recursive uses O(N) stack space; iterative uses O(1).
def sum_to_recursive(n):
    raise NotImplementedError


def sum_to_iterative(n):
    raise NotImplementedError


def recursion_limit():
    raise NotImplementedError
# ==== END


# ==== EX 19.4 | Reverse an array without extra space | Core
# PROMPT: Write `reverse_copy(arr)` (new list) and compare with your 1.16 `reverse_in_place`. Which would you use for a 1 GB list?
# EXAMPLE: `[1, 2, 3]` -> `[3, 2, 1]`
# BIGO: Copy: O(N) time, O(N) space. In place: O(N) time, O(1) space.
def reverse_copy(arr):
    raise NotImplementedError
# ==== END


# ==== EX 19.5 | Palindrome in O(1) space | Practice
# PROMPT: `s == s[::-1]` builds a full reversed copy. Write `is_palindrome_clean(s)` that ignores case and anything that is not a letter or digit, using two pointers and no new string.
# EXAMPLE: `'A man, a plan, a canal: Panama'` -> `True`
# BIGO: O(N) time, O(1) extra space.
def is_palindrome_clean(s):
    raise NotImplementedError
# ==== END
