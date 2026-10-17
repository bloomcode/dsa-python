"""Chapter 29: Monte Carlo and Las Vegas algorithms."""
import math


# ==== EX 29.1 | Estimate pi by throwing darts | Core
# PROMPT: Write `estimate_pi(samples, rng)`: pick random points in the unit square and return 4 times the fraction that land inside the quarter circle.
# EXAMPLE: `estimate_pi(100_000, random.Random(0))` -> about `3.14` (within 0.02)
# BIGO: O(S) samples; the error shrinks like 1 / sqrt(S), so 100 times more samples buy one more correct digit.
def estimate_pi(samples, rng):
    raise NotImplementedError
# ==== END


# ==== EX 29.2 | Averages from a random sample | Core
# PROMPT: Write `sampled_mean(data, k, rng)` estimating the mean of a huge list from k random positions (with replacement), and `exact_mean(data)` for comparison.
# EXAMPLE: one million values, k = 2,000 -> the estimate lands within about 2% of the true mean
# BIGO: O(k) instead of O(N); accuracy depends on k and the data's spread, not on N.
def sampled_mean(data, k, rng):
    raise NotImplementedError


def exact_mean(data):
    raise NotImplementedError
# ==== END


# ==== EX 29.3 | Monte Carlo versus Las Vegas | Core
# PROMPT: In a list where half the entries are 1, write `las_vegas_find_one(arr, rng)` (probe random positions until a 1 appears; always right, time varies) and `monte_carlo_find_one(arr, rng, tries)` (give up after `tries` probes and return -1; time fixed, may fail).
# EXAMPLE: both return an index holding 1; Monte Carlo with 20 tries fails with probability (1/2)^20, about one in a million
# BIGO: Las Vegas: 2 probes expected. Monte Carlo: exactly `tries` probes at most.
def las_vegas_find_one(arr, rng):
    raise NotImplementedError


def monte_carlo_find_one(arr, rng, tries):
    raise NotImplementedError
# ==== END


# ==== EX 29.4 | The trial-division baseline | Core
# PROMPT: Write `is_prime_trial(n)` checking divisors up to sqrt(n). Time it on a 12-digit prime and note why it is too slow for 100-digit numbers.
# EXAMPLE: `is_prime_trial(999_999_000_001)` -> `True` after about 500,000 divisions
# BIGO: O(sqrt N): exponential in the number of digits.
def is_prime_trial(n):
    raise NotImplementedError
# ==== END


# ==== EX 29.5 | Fermat's little theorem, one base | Core
# PROMPT: If n is prime, `pow(a, n - 1, n) == 1` for every a not divisible by n. Write `fermat_witness(a, n)` returning True when a proves n composite.
# EXAMPLE: `fermat_witness(2, 15)` -> `True` (15 is composite); `fermat_witness(2, 13)` -> `False`
# BIGO: O(log n) multiplications with three-argument pow.
def fermat_witness(a, n):
    raise NotImplementedError
# ==== END


# ==== EX 29.6 | Fermat's primality test | Core
# PROMPT: Write `fermat_test(n, k, rng)` trying k random bases in [2, n - 2] and answering "probably prime" (True) if none is a witness. Then show 561, a Carmichael number, fools every base coprime to it.
# EXAMPLE: `fermat_test(10**9 + 7, 20, rng)` -> `True`; `fermat_test(1_000_000_007 * 998_244_353, 20, rng)` -> `False`; `fermat_witness(2, 561)` -> `False` although 561 = 3 x 11 x 17
# BIGO: O(k log n). A Monte Carlo algorithm: "composite" is always right, "prime" can be wrong.
def fermat_test(n, k, rng):
    raise NotImplementedError
# ==== END


# ==== EX 29.7 | Miller-Rabin, which Carmichael numbers cannot fool | Stretch
# PROMPT: Write `miller_rabin(n, bases=(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37))`: write n - 1 = d x 2^s, and for each base check whether `a^d` is 1 or reaches n - 1 by repeated squaring. With these 12 bases it is exact for every n below 3.3 x 10^24.
# EXAMPLE: `miller_rabin(561)` -> `False`; `miller_rabin(2**61 - 1)` -> `True`
# BIGO: O(k log^3 n) bit operations; effectively instant for 64-bit numbers.
def miller_rabin(n, bases=(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)):
    raise NotImplementedError
# ==== END


# ==== EX 29.8 | Simulate, then check against the formula | Practice
# PROMPT: Write `birthday_simulation(people, trials, rng)` estimating the chance that two of `people` share a birthday (365 days), and `birthday_exact(people)` from the product formula.
# EXAMPLE: 23 people -> exact `0.507...`; 20,000 simulated trials land within 0.02 of it
# BIGO: O(trials x people). When no formula exists, simulation is how you get the number.
def birthday_simulation(people, trials, rng):
    raise NotImplementedError


def birthday_exact(people):
    raise NotImplementedError
# ==== END
