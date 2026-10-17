"""Chapter 23: Randomness as a tool.

Every function that needs randomness takes an `rng` (a `random.Random`), so results
are reproducible in tests and you can see the same "random" run twice.
"""
import bisect
import itertools
import random
from collections import Counter


# ==== EX 23.1 | Randomized quicksort | Core
# PROMPT: Write `random_quicksort(arr, rng)` returning a new sorted list, choosing each pivot uniformly at random. Count comparisons on sorted input and compare with 22.6.
# EXAMPLE: `random_quicksort(list(range(10)), random.Random(1))` -> `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
# BIGO: O(N log N) expected on every input, including sorted ones. The worst case still exists but needs extraordinarily bad luck.
def random_quicksort(arr, rng):
    raise NotImplementedError
# ==== END


# ==== EX 23.2 | Reproducible randomness with seeds | Core
# PROMPT: Write `sample_with_seed(seed, population, k)` that returns the same k-item sample every time for the same seed, using its own `random.Random(seed)` rather than the global generator.
# EXAMPLE: `sample_with_seed(42, range(100), 3) == sample_with_seed(42, range(100), 3)` -> `True`
# BIGO: O(k).
# NOTE: A private `Random` instance keeps your results reproducible even when other code also draws random numbers.
def sample_with_seed(seed, population, k):
    raise NotImplementedError
# ==== END


# ==== EX 23.3 | A linear congruential generator | Core
# PROMPT: Write a generator `lcg(seed, a=1103515245, c=12345, m=2**31)` yielding `x = (a * x + c) % m` forever. Then find the period of the tiny generator `a=5, c=3, m=16`.
# EXAMPLE: first three values from `lcg(1, 5, 3, 16)` -> `[8, 11, 10]`; its period is `16`
# BIGO: O(1) per number. This is a PRNG: fully determined by the seed, which is why it is reproducible and why it is not secure.
def lcg(seed, a=1103515245, c=12345, m=2**31):
    raise NotImplementedError


def lcg_period(seed, a, c, m):
    raise NotImplementedError
# ==== END


# ==== EX 23.4 | Fisher-Yates shuffle | Core
# PROMPT: Write `fisher_yates(arr, rng)` that shuffles in place: for i from the last index down to 1, swap arr[i] with arr[j] for a random j in 0..i.
# EXAMPLE: `fisher_yates([1, 2, 3, 4, 5], random.Random(7))` returns some ordering of 1..5, the same one every time for seed 7
# BIGO: O(N) time, O(1) extra space, and every permutation is equally likely.
def fisher_yates(arr, rng):
    raise NotImplementedError
# ==== END


# ==== EX 23.5 | Prove the naive shuffle is biased | Practice
# PROMPT: The naive shuffle swaps each position with any position 0..n-1. Write `naive_distribution(n)` and `fisher_yates_distribution(n)` that enumerate every possible sequence of random choices and count the resulting permutations.
# EXAMPLE: For n = 3: Fisher-Yates gives each of the 6 permutations exactly once; naive spreads 27 outcomes as `{4, 5, 5, 5, 4, 4}`
# BIGO: O(n^n) and O(n!) sequences: exact enumeration, no randomness needed.
# NOTE: 27 equally likely outcomes cannot split evenly over 6 permutations, so the naive shuffle must be biased.
def naive_distribution(n):
    raise NotImplementedError


def fisher_yates_distribution(n):
    raise NotImplementedError
# ==== END


# ==== EX 23.6 | Randomize before building a BST | Core
# PROMPT: Write `bst_height(keys)` that inserts keys in order into a plain BST and returns its height. Compare sorted keys with the same keys shuffled.
# EXAMPLE: `bst_height(list(range(200)))` -> `200`; shuffled with `random.Random(3)` -> about 15 to 20
# BIGO: Height O(N) for sorted input, O(log N) expected after shuffling.
def bst_height(keys):
    raise NotImplementedError
# ==== END


# ==== EX 23.7 | Reservoir sampling | Practice
# PROMPT: Write `reservoir(stream, k, rng)` that picks k items uniformly from a stream of unknown length in one pass: keep the first k, then replace a random slot with item i (0-based) with probability k / (i + 1).
# EXAMPLE: `reservoir(range(1_000_000), 3, random.Random(0))` -> 3 values, each equally likely to be any of the million
# BIGO: O(N) time, O(k) memory.
def reservoir(stream, k, rng):
    raise NotImplementedError
# ==== END


# ==== EX 23.8 | Load balancing with random choices | Core
# PROMPT: Write `max_load_random(jobs, servers, rng)` assigning each job to a random server, and `max_load_two_choices(jobs, servers, rng)` picking two random servers and using the less loaded one. Return the busiest server's load.
# EXAMPLE: With 10,000 jobs on 1,000 servers and seed 5, two choices gives a clearly lower maximum than one choice
# BIGO: O(J) for J jobs. The "power of two choices" drops the expected maximum excess from about log N / log log N to log log N.
def max_load_random(jobs, servers, rng):
    raise NotImplementedError


def max_load_two_choices(jobs, servers, rng):
    raise NotImplementedError
# ==== END


# ==== EX 23.9 | Weighted random choice | Practice
# PROMPT: Write `make_weighted_picker(weights, rng)` that precomputes prefix sums and returns a function picking index i with probability weights[i] / total, using `bisect`.
# EXAMPLE: weights `[1, 3, 6]` -> over 10,000 picks index 2 comes up about 60% of the time
# BIGO: O(N) setup, O(log N) per pick.
def make_weighted_picker(weights, rng):
    raise NotImplementedError
# ==== END
