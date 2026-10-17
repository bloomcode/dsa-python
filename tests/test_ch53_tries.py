from ch53_tries import RankedTrie, Trie


def trie(*words):
    t = Trie()
    for w in words:
        t.insert(w)
    return t


def test_ex_53_1():
    t = trie('pin', 'pit')
    assert list(t.root.children) == ['p'] and set(t.root.children['p'].children['i'].children) == {'n', 't'}
    assert '*' in t.root.children['p'].children['i'].children['n'].children


def test_ex_53_2():
    t = trie('pin', 'pit')
    assert t.search('pi') is not None and t.search('po') is None


def test_ex_53_3():
    t = trie('pin', 'pit')
    assert t.contains_word('pin') and not t.contains_word('pi')


def test_ex_53_4():
    assert trie('pin', 'pit', 'sun').collect_all_words() == ['pin', 'pit', 'sun']
    assert Trie().collect_all_words() == []


def test_ex_53_5():
    t = trie('pin', 'pinch', 'pit', 'sun')
    assert t.autocomplete('pin') == ['pin', 'pinch'] and t.autocomplete('x') == []


def test_ex_53_6():
    assert trie('pie', 'pin').all_keys() == ['p', 'i', 'e', 'n']


def test_ex_53_7():
    assert trie('pine', 'pint', 'pinto').longest_common_prefix() == 'pin'
    assert trie('pin', 'pinch').longest_common_prefix() == 'pin' and trie('sun').longest_common_prefix() == 'sun'
    assert trie('pin', 'sun').longest_common_prefix() == '' and Trie().longest_common_prefix() == ''


def test_ex_53_8():
    r = RankedTrie()
    r.insert('pinch', 9)
    r.insert('pin', 5)
    r.insert('pinball', 7)
    assert r.autocomplete('pin', 2) == ['pinch', 'pinball'] and r.autocomplete('z') == []


def test_ex_53_9():
    t = trie('pin', 'pinto', 'pinch')
    assert t.delete('pinch') and t.contains_word('pin') and not t.contains_word('pinch')
    assert 'c' not in t.search('pin').children and t.contains_word('pinto')
    assert not t.delete('sun') and not t.delete('pi')
