import random

from ch29_monte_carlo import (birthday_exact, birthday_simulation, estimate_pi, exact_mean, fermat_test,
                              fermat_witness, is_prime_trial, las_vegas_find_one, miller_rabin,
                              monte_carlo_find_one, sampled_mean)


def test_ex_29_1():
    assert abs(estimate_pi(100_000, random.Random(0)) - 3.14159) < 0.02


def test_ex_29_2():
    rng = random.Random(4)
    data = [rng.randint(0, 1000) for _ in range(10**6)]
    assert abs(sampled_mean(data, 2000, random.Random(1)) / exact_mean(data) - 1) < 0.04
    assert exact_mean([1, 2, 3, 6]) == 3


def test_ex_29_3():
    arr = [i % 2 for i in range(1000)]
    assert arr[las_vegas_find_one(arr, random.Random(2))] == 1
    i = monte_carlo_find_one(arr, random.Random(2), 20)
    assert i == -1 or arr[i] == 1
    assert monte_carlo_find_one([0] * 10, random.Random(2), 20) == -1


def test_ex_29_4():
    assert is_prime_trial(999_999_000_001) and not is_prime_trial(1) and not is_prime_trial(999_999_000_001 * 3)
    assert [n for n in range(20) if is_prime_trial(n)] == [2, 3, 5, 7, 11, 13, 17, 19]


def test_ex_29_5():
    assert fermat_witness(2, 15) and not fermat_witness(2, 13) and not fermat_witness(2, 561)


def test_ex_29_6():
    rng = random.Random(6)
    assert fermat_test(10**9 + 7, 20, rng) and not fermat_test(1_000_000_007 * 998_244_353, 20, rng)


def test_ex_29_7():
    assert miller_rabin(999_999_000_001)
    assert not miller_rabin(561) and miller_rabin(2**61 - 1) and not miller_rabin(1)
    for n in range(2, 3000):
        assert miller_rabin(n) == all(n % d for d in range(2, int(n ** 0.5) + 1))
    for c in (561, 1105, 1729, 2465, 2821, 6601):
        assert not miller_rabin(c)


def test_ex_29_8():
    assert abs(birthday_exact(23) - 0.5073) < 1e-3
    assert abs(birthday_simulation(23, 20000, random.Random(3)) - 0.5073) < 0.02
