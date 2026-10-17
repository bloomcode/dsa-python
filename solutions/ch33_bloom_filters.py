"""Chapter 33: Bloom filters.

Hashes come from `hashlib` so results are the same on every run (Python's built-in
`hash()` for strings changes between processes).
"""
import hashlib
import math


def _two_hashes(item):
    d = hashlib.sha256(str(item).encode()).digest()
    return int.from_bytes(d[:8], "big"), int.from_bytes(d[8:16], "big") | 1


# ==== EX 33.1 | k hash functions from two | Core
# PROMPT: Write `bit_positions(item, k, m)` returning k bit positions in [0, m) using double hashing: `(h1 + i * h2) % m` for i in 0..k-1, where h1 and h2 come from one SHA-256 digest.
# EXAMPLE: `bit_positions("cat", 3, 32)` -> three positions in 0..31, the same on every run
# BIGO: O(k) after one hash computation. Kirsch and Mitzenmacher showed this behaves as well as k independent hashes.
def bit_positions(item, k, m):
    raise NotImplementedError
# ==== END


# ==== EX 33.2 | A Bloom filter | Core | class=BloomFilter
# PROMPT: Write `BloomFilter(m, k)` with an m-bit `bytearray`, `add(item)` setting the item's k bits, and `might_contain(item)` returning True only if all k bits are set.
# EXAMPLE: add "apple" and "pear" -> `might_contain("apple")` is `True`; `might_contain("grape")` is almost certainly `False`
# BIGO: O(k) per operation; m bits of memory regardless of how large the items are.
# NOTE: "No" is always right. "Yes" means "probably": other items may have set those same bits.
class BloomFilter:
    def __init__(self, m, k):
        raise NotImplementedError

    def _set(self, i):
        raise NotImplementedError

    def _get(self, i):
        raise NotImplementedError

    def add(self, item):
        raise NotImplementedError

    def might_contain(self, item):
        raise NotImplementedError
# ==== END

    # ==== EX 33.7 | Union of two filters | Practice | class=BloomFilter
    # PROMPT: Add `union(other)` returning a new filter whose bits are the OR of both, for filters built with the same m and k.
    # EXAMPLE: filter A holds "x", filter B holds "y" -> the union might contain both
    # BIGO: O(m / 8). Handy for merging filters built on separate machines.
    def union(self, other):
        raise NotImplementedError
    # ==== END


# ==== EX 33.3 | Predict the false-positive rate | Core
# PROMPT: Write `false_positive_rate(n, m, k)` = `(1 - e^(-k n / m))^k`, the chance a never-added item looks present after n insertions.
# EXAMPLE: `false_positive_rate(1000, 10_000, 7)` -> about `0.0082` (under 1%)
# BIGO: O(1).
def false_positive_rate(n, m, k):
    raise NotImplementedError
# ==== END


# ==== EX 33.4 | Size a filter for a target error | Core
# PROMPT: Write `optimal_params(n, p)` returning `(m, k)`: bits `m = ceil(-n ln p / (ln 2)^2)` and hash count `k = round((m / n) ln 2)`.
# EXAMPLE: `optimal_params(1_000_000, 0.01)` -> `(9585059, 7)`: about 1.2 MB for a million items at 1% error
# BIGO: O(1). Each tenfold cut in p costs only about 4.8 more bits per item.
def optimal_params(n, p):
    raise NotImplementedError
# ==== END


# ==== EX 33.5 | Measure the real error | Core
# PROMPT: Write `measured_fp_rate(n, m, k, probes)`: add the strings "in-0" .. "in-{n-1}", then probe "out-0" .. "out-{probes-1}" (never added) and return the fraction reported present.
# EXAMPLE: `measured_fp_rate(1000, 10_000, 7, 20_000)` lands close to the 13.3 prediction (within about 0.005)
# BIGO: O((n + probes) * k).
def measured_fp_rate(n, m, k, probes):
    raise NotImplementedError
# ==== END


# ==== EX 33.6 | Duplicate detection in a stream | Core
# PROMPT: Write `stream_duplicates(items, m, k)` that reports items the filter says it has seen before. Then write `confirmed_duplicates(items, m, k)` that double-checks each report against an exact set, and count how many reports were false.
# EXAMPLE: a stream of 5,000 unique items plus 100 repeats with m = 64,000, k = 6 -> all 100 repeats reported, and only a handful of false alarms
# BIGO: O(N * k) time, m bits of space. Real systems (web crawlers, databases) use the filter to skip most exact lookups.
def stream_duplicates(items, m, k):
    raise NotImplementedError


def confirmed_duplicates(items, m, k):
    raise NotImplementedError
# ==== END


# ==== EX 33.8 | A counting Bloom filter that can delete | Stretch
# PROMPT: Write `CountingBloomFilter(m, k)` with a list of small counters instead of bits: `add` increments, `remove` decrements (only for items you added), and `might_contain` checks all counters are above zero.
# EXAMPLE: add "a", add "b", remove "a" -> `might_contain("a")` is `False` (barring collisions), `might_contain("b")` is `True`
# BIGO: O(k) per operation, at the cost of 4 to 8 bits per counter instead of 1.
class CountingBloomFilter:
    def __init__(self, m, k):
        raise NotImplementedError

    def add(self, item):
        raise NotImplementedError

    def remove(self, item):
        raise NotImplementedError

    def might_contain(self, item):
        raise NotImplementedError
# ==== END
