from ch03_big_o import all_pairs_steps, array_sum, halving_steps, is_leap_year, squares_needed, unique_pairs_steps


def test_ex_3_1():
    assert is_leap_year(2024) and not is_leap_year(1900) and is_leap_year(2000)
    assert not is_leap_year(2023)


def test_ex_3_2():
    assert array_sum([1, 2, 3, 4]) == 10 and array_sum([]) == 0


def test_ex_3_3():
    assert halving_steps(8) == 3 and halving_steps(1024) == 10 and halving_steps(1) == 0


def test_ex_3_4():
    assert squares_needed(1) == 1 and squares_needed(16) == 5 and squares_needed(17) == 6


def test_ex_3_5():
    assert all_pairs_steps(4) == 16 and unique_pairs_steps(4) == 6
