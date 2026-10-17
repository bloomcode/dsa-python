"""Chapter 41: Hash tables."""


# ==== EX 41.1 | Build a hash table with chaining | Core | class=HashTable
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


# ==== EX 41.2 | Build a word from letter tiles | Core
# PROMPT: Write `can_build(word, tiles)`: each character of `tiles` can be used once. Count the tiles in a dict, then spend them on the word.
# EXAMPLE: `'abba'`, `'aabbc'` -> `True`; `'abc'`, `'ab'` -> `False`
# BIGO: O(N + M): count the tiles once, then spend them. Nested loops would be O(N * M).
def can_build(word, tiles):
    raise NotImplementedError
# ==== END


# ==== EX 41.3 | Values in exactly one list | Core
# PROMPT: Write `in_exactly_one(a, b)` returning the values that appear in one list but not the other: first those from `a` in `a`'s order, then those from `b` in `b`'s order, each once.
# EXAMPLE: `[1, 2, 3]`, `[2, 3, 4]` -> `[1, 4]`
# BIGO: O(N + M) with two sets, versus O(N * M) checking each value against the other list.
def in_exactly_one(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 41.4 | Distinct visitors per day | Core
# PROMPT: Visit `i` was on day `days[i]` by user `users[i]`. Write `distinct_per_day(days, users)` returning a dict from each day to the number of different users that day.
# EXAMPLE: `[1, 1, 1, 2]`, `['ana', 'bo', 'ana', 'ana']` -> `{1: 2, 2: 1}`
# BIGO: O(N): one set of visitors per day, one insert per visit.
def distinct_per_day(days, users):
    raise NotImplementedError
# ==== END


# ==== EX 41.5 | Same letter pattern | Practice
# PROMPT: Write `same_pattern(a, b)`: `True` when the letters of `a` can be renamed one-to-one to give `b` (equal letters stay equal, different letters stay different).
# EXAMPLE: `'egg'`, `'add'` -> `True`; `'foo'`, `'bar'` -> `False`
# BIGO: O(N) with two lookup tables, one for each direction.
def same_pattern(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 41.6 | Every position of each value | Core
# PROMPT: Write `positions(items)` returning a dict from each value to the list of indexes where it appears, in increasing order.
# EXAMPLE: `['a', 'b', 'a']` -> `{'a': [0, 2], 'b': [1]}`
# BIGO: O(N): one append per item.
def positions(items):
    raise NotImplementedError
# ==== END


# ==== EX 41.7 | Word frequency | Core
# PROMPT: Write `word_counts(text)` returning a dict of lowercase word to count, and `most_common_word(text)`.
# EXAMPLE: `'the cat and the hat'` -> `{'the': 2, 'cat': 1, 'and': 1, 'hat': 1}`, most common `'the'`
# BIGO: O(N) in the number of words.
def word_counts(text):
    raise NotImplementedError


def most_common_word(text):
    raise NotImplementedError
# ==== END


# ==== EX 41.8 | Group anagrams | Practice
# PROMPT: Write `group_anagrams(words)` returning lists of words that are anagrams of each other (groups in first-seen order).
# EXAMPLE: `['eat', 'tea', 'tan', 'ate', 'nat', 'bat']` -> `[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]`
# BIGO: O(N * K log K) for N words of length K: the sorted letters are the hash key.
def group_anagrams(words):
    raise NotImplementedError
# ==== END


# ==== EX 41.9 | Two sum with a lookup table | Core
# PROMPT: Write `two_sum_indices(nums, target)` returning the indices `(i, j)` of two numbers that add to `target`, or `None`.
# EXAMPLE: `[2, 7, 11, 15]`, target `9` -> `(0, 1)`
# BIGO: O(N) time, O(N) space; nested loops would be O(N^2).
def two_sum_indices(nums, target):
    raise NotImplementedError
# ==== END


# ==== EX 41.10 | Invert a lookup table | Practice
# PROMPT: Write `invert(menu)` turning `{item: price}` into `{price: [items]}` so you can look up everything at a price in one step.
# EXAMPLE: `{'fries': 2, 'soda': 2, 'burger': 5}` -> `{2: ['fries', 'soda'], 5: ['burger']}`
# BIGO: O(N) to build; every later lookup by price is O(1).
# NOTE: A hash table is one-directional: fast from key to value, slow from value to key. Build a second table when you need both.
def invert(menu):
    raise NotImplementedError
# ==== END
