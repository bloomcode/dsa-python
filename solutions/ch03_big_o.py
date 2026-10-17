"""Chapter 3: Big O: how the step count grows."""


# ==== EX 3.1 | An O(1) algorithm | Core
# PROMPT: Write `is_leap_year(year)`. Explain why its step count does not depend on the input's size.
# EXAMPLE: `is_leap_year(2024)` -> `True`; `1900` -> `False`; `2000` -> `True`
# BIGO: O(1). At most three checks, whatever the year.
def is_leap_year(year):
    raise NotImplementedError
# ==== END


# ==== EX 3.2 | An O(N) algorithm | Core
# PROMPT: Write `array_sum(arr)` with a loop (no `sum()`), and say how many steps it takes for N elements.
# EXAMPLE: `[1, 2, 3, 4]` -> `10`, 4 loop steps
# BIGO: O(N). One step per element.
def array_sum(arr):
    raise NotImplementedError
# ==== END


# ==== EX 3.3 | An O(log N) algorithm | Core
# PROMPT: Write `halving_steps(n)` returning how many times you can halve `n` (integer division) before it reaches 1.
# EXAMPLE: `halving_steps(8)` -> `3`; `halving_steps(1024)` -> `10`; `halving_steps(1)` -> `0`
# BIGO: O(log N). This is the definition of log2 N for powers of two.
def halving_steps(n):
    raise NotImplementedError
# ==== END


# ==== EX 3.4 | Doubling: grains on a chessboard | Practice
# PROMPT: One grain on square 1, two on square 2, four on square 3, and so on. Write `squares_needed(grains)` returning which square first holds at least `grains`.
# EXAMPLE: `squares_needed(1)` -> `1`; `squares_needed(16)` -> `5`; `squares_needed(17)` -> `6`
# BIGO: O(log N). The loop doubles a counter until it reaches N, the mirror image of halving.
def squares_needed(grains):
    raise NotImplementedError
# ==== END


# ==== EX 3.5 | Count nested-loop steps | Practice
# PROMPT: Write `all_pairs_steps(n)` (inner loop runs N times per outer step) and `unique_pairs_steps(n)` (inner loop starts at `i + 1`). Both return the number of inner-loop iterations. Classify both.
# EXAMPLE: `all_pairs_steps(4)` -> `16`; `unique_pairs_steps(4)` -> `6`
# BIGO: Both O(N^2). Unique pairs is N(N-1)/2, about half, and Big O ignores the 1/2.
def all_pairs_steps(n):
    raise NotImplementedError


def unique_pairs_steps(n):
    raise NotImplementedError
# ==== END
