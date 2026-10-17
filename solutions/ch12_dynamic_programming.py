"""Chapter 12: Dynamic programming: memoize or build up."""


# ==== EX 12.1 | Fibonacci three ways | Core
# PROMPT: Write `fib_naive(n)`, `fib_memo(n, memo=None)` and `fib_bottom_up(n)`, with fib(0) = 0 and fib(1) = 1.
# EXAMPLE: All three return `55` for `n = 10`; only the last two finish quickly for `n = 80`
# BIGO: Naive O(2^N); memoised O(N) time and space; bottom-up O(N) time and O(1) space.
# NOTE: Pass `memo` explicitly rather than using a mutable default argument, which would be shared across calls.
def fib_naive(n):
    raise NotImplementedError


def fib_memo(n, memo=None):
    raise NotImplementedError


def fib_bottom_up(n):
    raise NotImplementedError
# ==== END


# ==== EX 12.2 | Fix the double recursive call | Core
# PROMPT: This version of max calls itself twice per level: `return arr[0] if arr[0] > max_bad(arr[1:]) else max_bad(arr[1:])`. Write `max_recursive(arr)` that calls itself once per level.
# EXAMPLE: `[1, 2, 3, 4]` -> `4`
# BIGO: From O(2^N) to O(N), just by storing the recursive result in a variable.
def max_recursive(arr):
    raise NotImplementedError
# ==== END


# ==== EX 12.3 | Staircase with memoization | Core
# PROMPT: Rewrite 11.8 as `staircase_memo(n, memo=None)`.
# EXAMPLE: `staircase_memo(5)` -> `13`; `staircase_memo(50)` returns at once
# BIGO: O(N).
def staircase_memo(n, memo=None):
    raise NotImplementedError
# ==== END


# ==== EX 12.4 | Unique paths with memoization | Core
# PROMPT: Rewrite 11.10 as `unique_paths_memo(rows, cols, memo=None)`, keyed by `(rows, cols)`.
# EXAMPLE: `unique_paths_memo(3, 7)` -> `28`; `(18, 18)` -> `2333606220`
# BIGO: O(rows * cols): each sub-grid is solved once.
def unique_paths_memo(rows, cols, memo=None):
    raise NotImplementedError
# ==== END


# ==== EX 12.5 | Count the calls | Practice
# PROMPT: Write `count_fib_calls(n)` returning `(naive_calls, memo_calls)`: how many times each Fibonacci version is invoked.
# EXAMPLE: `count_fib_calls(10)` -> `(177, 19)`
# BIGO: Shows overlapping subproblems directly: naive calls grow about 1.6x per step of n, memo calls by 2.
def count_fib_calls(n):
    raise NotImplementedError
# ==== END


# ==== EX 12.6 | Fewest coins, bottom-up | Stretch
# PROMPT: Write `min_coins(coins, amount)` filling a table `best[0..amount]` from the bottom up. Return `-1` if the amount cannot be made.
# EXAMPLE: `[1, 5, 10, 25]`, 63 -> `6`; `[2]`, 3 -> `-1`
# BIGO: O(amount * number of coins) time, O(amount) space.
# NOTE: Greedy (largest coin first) fails for coins like `[1, 3, 4]` and amount 6: greedy gives 3 coins, the answer is 2.
def min_coins(coins, amount):
    raise NotImplementedError
# ==== END
