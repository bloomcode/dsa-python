"""Chapter 32: Bit vectors: one bit per member."""
import sys


# ==== EX 32.1 | A set as a boolean array | Core
# PROMPT: Write `BoolArraySet(universe)` for integers 0..universe-1 backed by a list of booleans, with `add`, `remove`, `__contains__` and `__len__`.
# EXAMPLE: universe 10: add 3, add 7, remove 3 -> `7 in s` is `True`, `3 in s` is `False`, `len(s)` is `1`
# BIGO: O(1) per operation, but one Python object slot (8 bytes) per possible value.
class BoolArraySet:
    def __init__(self, universe):
        raise NotImplementedError

    def add(self, x):
        raise NotImplementedError

    def remove(self, x):
        raise NotImplementedError

    def __contains__(self, x):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError
# ==== END


# ==== EX 32.2 | A bit vector with masks | Core | class=BitVector
# PROMPT: Write `BitVector(size)` on a `bytearray` of ceil(size / 8) bytes. Value x lives in byte `x >> 3`, bit `x & 7`. Implement `add` (OR with the mask), `remove` (AND with the inverted mask) and `__contains__` (AND, then test).
# EXAMPLE: `bv = BitVector(100); bv.add(42)` -> `42 in bv` is `True`; `bv.data[5]` is `4` (bit 2 of byte 5)
# BIGO: O(1) per operation, and 1 bit per possible value: 64 times less than a list of booleans.
class BitVector:
    def __init__(self, size):
        raise NotImplementedError

    def add(self, x):
        raise NotImplementedError

    def remove(self, x):
        raise NotImplementedError

    def __contains__(self, x):
        raise NotImplementedError
# ==== END

    # ==== EX 32.3 | Count the members | Core | class=BitVector
    # PROMPT: Add `__len__` that counts set bits across all bytes, using `int.bit_count` on each byte (or a 256-entry lookup table).
    # EXAMPLE: add 1, 5, 99 -> `len(bv)` is `3`
    # BIGO: O(size / 8). Keep a running counter instead if you need O(1).
    def __len__(self):
        raise NotImplementedError
    # ==== END

    # ==== EX 32.4 | Union, intersection and difference | Core | class=BitVector
    # PROMPT: Add `union`, `intersection` and `difference`, each returning a new `BitVector` of the same size by combining the bytes with `|`, `&` and `& ~`.
    # EXAMPLE: {1, 2, 3} and {2, 3, 4} -> union `{1, 2, 3, 4}`, intersection `{2, 3}`, difference `{1}`
    # BIGO: O(size / 8): eight set members combined per byte operation.
    def _combine(self, other, op):
        raise NotImplementedError

    def union(self, other):
        raise NotImplementedError

    def intersection(self, other):
        raise NotImplementedError

    def difference(self, other):
        raise NotImplementedError
    # ==== END

    # ==== EX 32.5 | Iterate over members | Core | class=BitVector
    # PROMPT: Add `__iter__` yielding members in increasing order, skipping zero bytes entirely.
    # EXAMPLE: add 9, 2, 63 -> `list(bv)` is `[2, 9, 63]`
    # BIGO: O(size / 8 + members).
    def __iter__(self):
        raise NotImplementedError
    # ==== END


# ==== EX 32.6 | Estimate the space | Core
# PROMPT: Write `space_report(n)` returning the bytes used by a Python `set` of 0..n-1 (the set plus its int objects), a list of n booleans, and a `BitVector(n)`.
# EXAMPLE: n = 1,000,000 -> set about 60 MB, list about 8 MB, bit vector `125000` bytes
# BIGO: O(N) each, but the constants differ by a factor of about 500.
def space_report(n):
    raise NotImplementedError
# ==== END


# ==== EX 32.7 | Find duplicates in a bounded range | Core
# PROMPT: Write `first_duplicate(nums, universe)` returning the first value seen twice, using a `BitVector` as the "seen" set.
# EXAMPLE: `first_duplicate([4, 9, 1, 9, 4], 10)` -> `9`; no repeats -> `None`
# BIGO: O(N) time, universe / 8 bytes of space, no matter how many numbers there are.
def first_duplicate(nums, universe):
    raise NotImplementedError
# ==== END


# ==== EX 32.8 | A built-in type as a growable bit set | Practice
# PROMPT: Write `IntBitSet` holding one Python int: `add` with `|=`, `__contains__` with `>>` and `&`, `__or__` and `__and__` for set operations, and `__len__` with `bit_count`.
# EXAMPLE: `a = IntBitSet([1, 5]); b = IntBitSet([5, 7])` -> `list(a | b)` is `[1, 5, 7]`; `len(a & b)` is `1`
# BIGO: Big-int operations run in O(size / 64) machine words, and the set grows as needed.
class IntBitSet:
    def __init__(self, items=()):
        raise NotImplementedError

    def add(self, x):
        raise NotImplementedError

    def __contains__(self, x):
        raise NotImplementedError

    def __or__(self, other):
        raise NotImplementedError

    def __and__(self, other):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError
# ==== END


# ==== EX 32.9 | Missing numbers from a range | Practice
# PROMPT: Write `missing(nums, n)` returning every value in 0..n-1 that does not appear in `nums`, marking a `BitVector` and then scanning it.
# EXAMPLE: `missing([0, 3, 1, 6], 7)` -> `[2, 4, 5]`
# BIGO: O(N + n) time, n / 8 bytes of space.
def missing(nums, n):
    raise NotImplementedError
# ==== END
