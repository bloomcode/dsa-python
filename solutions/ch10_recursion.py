"""Chapter 10: Recursion: a base case and a smaller problem."""


# ==== EX 10.1 | Countdown | Core
# PROMPT: Write `countdown(n)` recursively, returning the list from n down to 0. Identify the base case first.
# EXAMPLE: `countdown(3)` -> `[3, 2, 1, 0]`
# BIGO: O(N) time, O(N) call-stack depth.
def countdown(n):
    raise NotImplementedError
# ==== END


# ==== EX 10.2 | Factorial | Core
# PROMPT: Write `factorial(n)` recursively.
# EXAMPLE: `factorial(5)` -> `120`; `factorial(0)` -> `1`
# BIGO: O(N).
def factorial(n):
    raise NotImplementedError
# ==== END


# ==== EX 10.3 | Sum an array recursively | Core
# PROMPT: Write `sum_recursive(arr, index=0)` without slicing (slicing copies, adding hidden O(N) work per call).
# EXAMPLE: `[1, 2, 3, 4]` -> `10`
# BIGO: O(N) time and stack depth.
def sum_recursive(arr, index=0):
    raise NotImplementedError
# ==== END


# ==== EX 10.4 | Flatten nested lists | Core
# PROMPT: Write `flatten(nested)` returning every number in a list that may contain lists to any depth, in order.
# EXAMPLE: `[1, [2, [3, 4]], 5]` -> `[1, 2, 3, 4, 5]`
# BIGO: O(N) in the total number of items. Recursion fits because the depth is unknown in advance.
def flatten(nested):
    raise NotImplementedError
# ==== END


# ==== EX 10.5 | Fast power | Practice
# PROMPT: Write `power(x, n)` for integer `n >= 0` by squaring: x^n = (x^(n//2))^2, times x if n is odd.
# EXAMPLE: `power(2, 10)` -> `1024`; `power(3, 0)` -> `1`
# BIGO: O(log N): each call halves n.
def power(x, n):
    raise NotImplementedError
# ==== END


# ==== EX 10.6 | Filesystem traversal | Core
# PROMPT: Model a filesystem as nested dicts (`{name: subtree}`; files map to `None`). Write `all_directories(tree, path='')` returning every directory path, depth first.
# EXAMPLE: `{'docs': {'old': {}, 'a.txt': None}, 'src': {}}` -> `['/docs', '/docs/old', '/src']`
# BIGO: O(N) in the number of entries.
# NOTE: The real version swaps the dict for `os.scandir(path)` and `entry.is_dir()`: same shape, same recursion.
def all_directories(tree, path=""):
    raise NotImplementedError
# ==== END


# ==== EX 10.7 | Every number from low to high | Core
# PROMPT: Write `numbers_between(low, high)` recursively returning `[low, ..., high]`.
# EXAMPLE: `numbers_between(3, 6)` -> `[3, 4, 5, 6]`
# BIGO: O(N).
def numbers_between(low, high):
    raise NotImplementedError
# ==== END
