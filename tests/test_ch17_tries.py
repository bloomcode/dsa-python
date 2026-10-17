from ch17_tries import RankedTrie, Trie


def trie(*words):
    t = Trie()
    for w in words:
        t.insert(w)
    return t


def test_ex_17_1():
    t = trie('cat', 'cab')
    assert list(t.root.children) == ['c'] and set(t.root.children['c'].children['a'].children) == {'t', 'b'}
    assert '*' in t.root.children['c'].children['a'].children['t'].children


def test_ex_17_2():
    t = trie('cat', 'cab')
    assert t.search('ca') is not None and t.search('co') is None


def test_ex_17_3():
    t = trie('cat', 'cab')
    assert t.contains_word('cat') and not t.contains_word('ca')


def test_ex_17_4():
    assert trie('cat', 'cab', 'dog').collect_all_words() == ['cat', 'cab', 'dog']
    assert Trie().collect_all_words() == []


def test_ex_17_5():
    t = trie('cat', 'catnip', 'cab', 'dog')
    assert t.autocomplete('cat') == ['cat', 'catnip'] and t.autocomplete('x') == []


def test_ex_17_6():
    assert trie('can', 'cat').all_keys() == ['c', 'a', 'n', 't']


def test_ex_17_7():
    t = trie('cat', 'catnap', 'catnip')
    assert t.autocorrect('catnar') == 'catnap' and t.autocorrect('cat') == 'cat'


def test_ex_17_8():
    r = RankedTrie()
    r.insert('catnip', 9)
    r.insert('cat', 5)
    r.insert('catalog', 7)
    assert r.autocomplete('cat', 2) == ['catnip', 'catalog'] and r.autocomplete('z') == []


def test_ex_17_9():
    t = trie('cat', 'catnap', 'catnip')
    assert t.delete('catnip') and t.contains_word('cat') and not t.contains_word('catnip')
    assert 'i' not in t.search('catn').children and t.contains_word('catnap')
    assert not t.delete('dog') and not t.delete('ca')
