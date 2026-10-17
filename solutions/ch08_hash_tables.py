"""Chapter 8: Hash tables and constant-time lookup."""


# ==== EX 8.1 | Build a hash table with chaining | Core | class=HashTable
# PROMPT: Build `HashTable` on a list of buckets (each a list of `[key, value]` pairs). Implement `put`, `get` (raise `KeyError` if missing), `delete`, `__contains__`, `__len__`. Double the bucket count when the load factor passes 0.75.
# EXAMPLE: `t.put('bad', 'evil'); t.get('bad')` -> `'evil'`; putting the same key again overwrites it
# BIGO: O(1) average for put, get and delete; O(N) worst case if every key collides into one bucket. A resize is O(N), but rare, so O(1) amortized.
# NOTE: Collisions are why buckets hold lists. A good table balances few collisions (more buckets) against wasted memory.
class HashTable:
    def __init__(self, capacity=8):
        raise NotImplementedError

    def _bucket(self, key):
        raise NotImplementedError

    def put(self, key, value):
        raise NotImplementedError

    def get(self, key):
        raise NotImplementedError

    def delete(self, key):
        raise NotImplementedError

    def __contains__(self, key):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def _resize(self):
        raise NotImplementedError
# ==== END


# ==== EX 8.2 | Is one array a subset of another? | Core
# PROMPT: Write `is_subset(small, big)` returning `True` if every value in `small` appears in `big`.
# EXAMPLE: `['b', 'd']`, `['a', 'b', 'c', 'd']` -> `True`
# BIGO: O(N + M) with a hash table, versus O(N * M) with nested loops.
def is_subset(small, big):
    raise NotImplementedError
# ==== END


# ==== EX 8.3 | Intersection in linear time | Core
# PROMPT: Write `intersection(a, b)` returning values present in both, in the order they appear in `a`, each once.
# EXAMPLE: `[1, 2, 3, 4, 5]`, `[0, 2, 4, 6, 8]` -> `[2, 4]`
# BIGO: O(N + M). Compare with 6.3's O(N * M).
def intersection(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 8.4 | First duplicate string | Core
# PROMPT: Write `first_duplicate(words)` returning the first word seen a second time, or `None`.
# EXAMPLE: `['a', 'b', 'c', 'd', 'c', 'e', 'f']` -> `'c'`
# BIGO: O(N).
def first_duplicate(words):
    raise NotImplementedError
# ==== END


# ==== EX 8.5 | The missing letter | Practice
# PROMPT: A string contains every letter a-z except one. Write `missing_letter(s)` to find it.
# EXAMPLE: `'the quick brown box jumps over a lazy dog'` -> `'f'`
# BIGO: O(N): one pass to record letters, then a fixed 26 checks.
def missing_letter(s):
    raise NotImplementedError
# ==== END


# ==== EX 8.6 | First non-repeated character | Core
# PROMPT: Write `first_unique_char(s)` returning the first character that appears exactly once, or `None`.
# EXAMPLE: `'minimum'` -> `'n'`
# BIGO: O(N): two passes, counting then checking.
def first_unique_char(s):
    raise NotImplementedError
# ==== END


# ==== EX 8.7 | Word frequency | Core
# PROMPT: Write `word_counts(text)` returning a dict of lowercase word to count, and `most_common_word(text)`.
# EXAMPLE: `'the cat and the hat'` -> `{'the': 2, 'cat': 1, 'and': 1, 'hat': 1}`, most common `'the'`
# BIGO: O(N) in the number of words.
def word_counts(text):
    raise NotImplementedError


def most_common_word(text):
    raise NotImplementedError
# ==== END


# ==== EX 8.8 | Group anagrams | Practice
# PROMPT: Write `group_anagrams(words)` returning lists of words that are anagrams of each other (groups in first-seen order).
# EXAMPLE: `['eat', 'tea', 'tan', 'ate', 'nat', 'bat']` -> `[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]`
# BIGO: O(N * K log K) for N words of length K: the sorted letters are the hash key.
def group_anagrams(words):
    raise NotImplementedError
# ==== END


# ==== EX 8.9 | Two sum with a lookup table | Core
# PROMPT: Write `two_sum_indices(nums, target)` returning the indices `(i, j)` of two numbers that add to `target`, or `None`.
# EXAMPLE: `[2, 7, 11, 15]`, target `9` -> `(0, 1)`
# BIGO: O(N) time, O(N) space; nested loops would be O(N^2).
def two_sum_indices(nums, target):
    raise NotImplementedError
# ==== END


# ==== EX 8.10 | Invert a lookup table | Practice
# PROMPT: Write `invert(menu)` turning `{item: price}` into `{price: [items]}` so you can look up everything at a price in one step.
# EXAMPLE: `{'fries': 2, 'soda': 2, 'burger': 5}` -> `{2: ['fries', 'soda'], 5: ['burger']}`
# BIGO: O(N) to build; every later lookup by price is O(1).
# NOTE: A hash table is one-directional: fast from key to value, slow from value to key. Build a second table when you need both.
def invert(menu):
    raise NotImplementedError
# ==== END
