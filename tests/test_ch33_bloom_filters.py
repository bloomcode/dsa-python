from ch33_bloom_filters import (BloomFilter, CountingBloomFilter, bit_positions, confirmed_duplicates,
                                false_positive_rate, measured_fp_rate, optimal_params, stream_duplicates)


def test_ex_33_1():
    assert bit_positions("cat", 3, 32) == bit_positions("cat", 3, 32)
    assert len(bit_positions("cat", 3, 32)) == 3 and all(0 <= p < 32 for p in bit_positions("cat", 3, 32))


def test_ex_33_2():
    bf = BloomFilter(1000, 5)
    bf.add("apple")
    bf.add("pear")
    assert bf.might_contain("apple") and bf.might_contain("pear") and not bf.might_contain("grape")
    bf2 = BloomFilter(5000, 4)
    for i in range(300):
        bf2.add(f"w{i}")
    assert all(bf2.might_contain(f"w{i}") for i in range(300))


def test_ex_33_3():
    assert abs(false_positive_rate(1000, 10_000, 7) - 0.0082) < 0.0005


def test_ex_33_4():
    assert optimal_params(1_000_000, 0.01) == (9585059, 7)


def test_ex_33_5():
    measured = measured_fp_rate(1000, 10_000, 7, 20_000)
    assert abs(measured - 0.0082) < 0.005


def test_ex_33_6():
    items = [f"u{i}" for i in range(5000)] + [f"u{i}" for i in range(0, 5000, 50)]
    reported = stream_duplicates(items, 64_000, 6)
    real, false_alarms = confirmed_duplicates(items, 64_000, 6)
    assert len(real) == 100 and false_alarms < 20 and len(reported) >= 100


def test_ex_33_7():
    a, b = BloomFilter(512, 3), BloomFilter(512, 3)
    a.add("x")
    b.add("y")
    u = a.union(b)
    assert u.might_contain("x") and u.might_contain("y")


def test_ex_33_8():
    cb = CountingBloomFilter(1000, 4)
    cb.add("a")
    cb.add("b")
    assert cb.remove("a") and not cb.might_contain("a") and cb.might_contain("b") and not cb.remove("zzz")
