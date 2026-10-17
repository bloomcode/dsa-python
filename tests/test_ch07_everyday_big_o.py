from ch07_everyday_big_o import (all_passwords, average_celsius, clothing_labels, count_ones, cross_products,
                                 is_palindrome, mean_of_evens, pair_products, sample, three_letter_words,
                                 two_letter_words)


def test_ex_7_1():
    assert mean_of_evens([1, 2, 3, 4, 6]) == 4.0 and mean_of_evens([1]) is None


def test_ex_7_2():
    assert two_letter_words(['a', 'b', 'c']) == ['ab', 'ac', 'ba', 'bc', 'ca', 'cb']


def test_ex_7_3():
    assert three_letter_words(['a', 'b', 'c']) == ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']


def test_ex_7_4():
    assert sample([1, 2, 3, 4, 5]) == [1, 3, 5]


def test_ex_7_5():
    assert average_celsius([32, 212]) == 50.0


def test_ex_7_6():
    labels = clothing_labels(['Shirt'])
    assert labels[0] == 'Shirt Size: 1' and labels[-1] == 'Shirt Size: 5' and len(labels) == 5


def test_ex_7_7():
    assert count_ones([[0, 1, 1], [1, 0], [1, 1, 1, 0]]) == 6


def test_ex_7_8():
    assert is_palindrome('racecar') and not is_palindrome('kayaks') and is_palindrome('')


def test_ex_7_9():
    assert pair_products([1, 2, 3, 4]) == [2, 3, 4, 6, 8, 12]


def test_ex_7_10():
    assert cross_products([1, 2], [10, 100, 1000]) == [10, 100, 1000, 20, 200, 2000]


def test_ex_7_11():
    assert list(all_passwords(2, 'ab')) == ['aa', 'ab', 'ba', 'bb']
    assert len(list(all_passwords(3))) == 26 ** 3
