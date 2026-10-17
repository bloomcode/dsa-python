"""Chapter 7: Big O in day-to-day code."""


# ==== EX 7.1 | Mean of the even numbers | Core
# PROMPT: Write `mean_of_evens(numbers)`. Return `None` if there are no even numbers.
# EXAMPLE: `[1, 2, 3, 4, 6]` -> `4.0`
# BIGO: O(N). The loop runs once per number, whatever happens inside.
def mean_of_evens(numbers):
    raise NotImplementedError
# ==== END


# ==== EX 7.2 | Word builder, two characters | Core
# PROMPT: Write `two_letter_words(chars)` returning every string made of two different positions in `chars`.
# EXAMPLE: `['a', 'b', 'c']` -> `['ab', 'ac', 'ba', 'bc', 'ca', 'cb']`
# BIGO: O(N^2).
def two_letter_words(chars):
    raise NotImplementedError
# ==== END


# ==== EX 7.3 | Word builder, three characters | Practice
# PROMPT: Extend to `three_letter_words(chars)` using three distinct positions. How does the Big O change?
# EXAMPLE: `['a', 'b', 'c']` -> 6 words: `'abc', 'acb', 'bac', 'bca', 'cab', 'cba'`
# BIGO: O(N^3). Each extra nested loop over the same input adds one to the exponent.
def three_letter_words(chars):
    raise NotImplementedError
# ==== END


# ==== EX 7.4 | Array sample | Core
# PROMPT: Write `sample(arr)` returning `[first, middle, last]` of a non-empty list.
# EXAMPLE: `[1, 2, 3, 4, 5]` -> `[1, 3, 5]`
# BIGO: O(1). Three reads by index, no matter how long the list is.
def sample(arr):
    raise NotImplementedError
# ==== END


# ==== EX 7.5 | Average Celsius reading | Core
# PROMPT: Write `average_celsius(fahrenheit)` that converts each reading with (F - 32) / 1.8 and returns the mean.
# EXAMPLE: `[32, 212]` -> `50.0`
# BIGO: O(N). Two loops one after another are 2N steps, still O(N); only nesting multiplies.
def average_celsius(fahrenheit):
    raise NotImplementedError
# ==== END


# ==== EX 7.6 | Clothing labels | Core
# PROMPT: Write `clothing_labels(items)` producing a label for every item in sizes 1 to 5.
# EXAMPLE: `['Shirt']` -> `['Shirt Size: 1', ..., 'Shirt Size: 5']`
# BIGO: O(N). The inner loop is a fixed 5, so it is 5N steps, not N^2.
def clothing_labels(items):
    raise NotImplementedError
# ==== END


# ==== EX 7.7 | Count the ones | Core
# PROMPT: Write `count_ones(rows)` for a list of lists of 0s and 1s.
# EXAMPLE: `[[0, 1, 1], [1, 0], [1, 1, 1, 0]]` -> `6`
# BIGO: O(N) where N is the total number of values, even though the loops are nested.
def count_ones(rows):
    raise NotImplementedError
# ==== END


# ==== EX 7.8 | Palindrome checker | Core
# PROMPT: Write `is_palindrome(s)` comparing characters from both ends inward. No slicing.
# EXAMPLE: `'racecar'` -> `True`; `'kayaks'` -> `False`
# BIGO: O(N) (N/2 comparisons).
def is_palindrome(s):
    raise NotImplementedError
# ==== END


# ==== EX 7.9 | Products of all pairs | Core
# PROMPT: Write `pair_products(nums)` returning the product of every unique pair (each pair once).
# EXAMPLE: `[1, 2, 3, 4]` -> `[2, 3, 4, 6, 8, 12]`
# BIGO: O(N^2): N(N-1)/2 pairs.
def pair_products(nums):
    raise NotImplementedError
# ==== END


# ==== EX 7.10 | Products across two arrays | Practice
# PROMPT: Write `cross_products(a, b)` returning `x * y` for every x in `a` and y in `b`.
# EXAMPLE: `[1, 2]`, `[10, 100, 1000]` -> `[10, 100, 1000, 20, 200, 2000]`
# BIGO: O(N * M). With two different inputs, name both sizes instead of writing O(N^2).
def cross_products(a, b):
    raise NotImplementedError
# ==== END


# ==== EX 7.11 | Password cracker | Practice
# PROMPT: Write a generator `all_passwords(length, alphabet='abcdefghijklmnopqrstuvwxyz')` that yields every string of that length, in order. Build it yourself before trying `itertools.product`.
# EXAMPLE: `list(all_passwords(2, 'ab'))` -> `['aa', 'ab', 'ba', 'bb']`
# BIGO: O(26^N). Exponential: each extra character multiplies the work by the alphabet size.
def all_passwords(length, alphabet="abcdefghijklmnopqrstuvwxyz"):
    raise NotImplementedError
# ==== END
