"""Chapter 72: Dynamic programming."""


# ==== EX 72.1 | Fibonacci three ways | Core
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


# ==== EX 72.2 | One recursive call per level | Core
# PROMPT: A version that finds the rest's minimum and its maximum with two separate recursive calls doubles the work at every level. Write `min_max(nums, i=0)` returning `(smallest, largest)` of `nums[i:]` for a non-empty list, with a single recursive call per level.
# EXAMPLE: `[4, -2, 9, 0]` -> `(-2, 9)`
# BIGO: From O(2^N) to O(N), just by keeping the one recursive result and reading both parts from it.
def min_max(nums, i=0):
    raise NotImplementedError
# ==== END


# ==== EX 72.3 | Tilings with memoization | Core
# PROMPT: Rewrite 71.15 as `tilings_memo(n, memo=None)`.
# EXAMPLE: `tilings_memo(10)` -> `28`; `tilings_memo(60)` -> `5582216355` at once
# BIGO: O(N): each length is solved once.
def tilings_memo(n, memo=None):
    raise NotImplementedError
# ==== END


# ==== EX 72.4 | Dice totals with memoization | Core
# PROMPT: Rewrite 71.17 as `dice_ways_memo(dice, total, memo=None)`, keyed by `(dice, total)`.
# EXAMPLE: `dice_ways_memo(2, 7)` -> `6`; `(20, 70)` -> `189456975899496`
# BIGO: O(D * T * 6) for D dice and total T: each (dice, total) pair is solved once, trying six faces.
def dice_ways_memo(dice, total, memo=None):
    raise NotImplementedError
# ==== END


# ==== EX 72.5 | Count the calls | Practice
# PROMPT: Write `count_fib_calls(n)` returning `(naive_calls, memo_calls)`: how many times each Fibonacci version is invoked.
# EXAMPLE: `count_fib_calls(10)` -> `(177, 19)`
# BIGO: Shows overlapping subproblems directly: naive calls grow about 1.6x per step of n, memo calls by 2.
def count_fib_calls(n):
    raise NotImplementedError
# ==== END


# ==== EX 72.6 | Fewest coins, bottom-up | Stretch
# PROMPT: Write `min_coins(coins, amount)` filling a table `best[0..amount]` from the bottom up. Return `-1` if the amount cannot be made.
# EXAMPLE: `[1, 5, 10, 25]`, 63 -> `6`; `[2]`, 3 -> `-1`
# BIGO: O(amount * number of coins) time, O(amount) space.
# NOTE: Greedy (largest coin first) fails for coins like `[1, 3, 4]` and amount 6: greedy gives 3 coins, the answer is 2.
def min_coins(coins, amount):
    raise NotImplementedError
# ==== END
