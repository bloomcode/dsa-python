"""Chapter 17: Tries for prefix search.

Each node holds a dict of children, and the key '*' marks the end of a word.
"""


# ==== EX 17.1 | Trie node and insertion | Core | class=Trie
# PROMPT: Create `TrieNode` with a `children` dict and `Trie` with a `root`. Write `insert(word)` that walks or creates one child per character, then adds a `'*'` child to mark the end of the word.
# EXAMPLE: insert 'cat', 'cab' -> root has one child `'c'`, whose `'a'` child has children `'t'` and `'b'`
# BIGO: O(K) for a K-character word, regardless of how many words are stored.
class TrieNode:
    def __init__(self):
        raise NotImplementedError


class Trie:
    def __init__(self):
        raise NotImplementedError

    def insert(self, word):
        raise NotImplementedError
# ==== END

    # ==== EX 17.2 | Search a prefix | Core | class=Trie
    # PROMPT: Add `search(prefix)` returning the node where the prefix ends, or `None` if it is not in the trie.
    # EXAMPLE: After 'cat' -> `search('ca')` is a node; `search('co')` is `None`
    # BIGO: O(K).
    def search(self, prefix):
        raise NotImplementedError
    # ==== END

    # ==== EX 17.3 | Is it a whole word? | Core | class=Trie
    # PROMPT: Add `contains_word(word)`: the prefix must exist and its node must have a `'*'` child.
    # EXAMPLE: After 'cat' -> `contains_word('cat')` is `True`, `contains_word('ca')` is `False`
    # BIGO: O(K).
    def contains_word(self, word):
        raise NotImplementedError
    # ==== END

    # ==== EX 17.4 | Collect every word | Core | class=Trie
    # PROMPT: Add `collect_all_words(node=None, word='', words=None)` that recursively gathers every word below `node` (the root by default).
    # EXAMPLE: After 'cat', 'cab', 'dog' -> `['cat', 'cab', 'dog']` (insertion order)
    # BIGO: O(M) for M nodes beneath the starting node.
    def collect_all_words(self, node=None, word="", words=None):
        raise NotImplementedError
    # ==== END

    # ==== EX 17.5 | Autocomplete | Core | class=Trie
    # PROMPT: Add `autocomplete(prefix)`: search to the prefix's node, collect the words below it and prepend the prefix.
    # EXAMPLE: Words 'cat', 'catnip', 'cab', 'dog' -> `autocomplete('cat')` -> `['cat', 'catnip']`
    # BIGO: O(K + M): reach the prefix, then visit only the matching subtree.
    def autocomplete(self, prefix):
        raise NotImplementedError
    # ==== END

    # ==== EX 17.6 | Print every key | Practice | class=Trie
    # PROMPT: Add `all_keys()` returning every character stored in the trie (excluding `'*'`), depth first.
    # EXAMPLE: After 'can', 'cat' -> `['c', 'a', 'n', 't']`
    # BIGO: O(M) nodes.
    def all_keys(self, node=None, keys=None):
        raise NotImplementedError
    # ==== END

    # ==== EX 17.7 | Autocorrect | Practice | class=Trie
    # PROMPT: Add `autocorrect(word)`: return the word if it exists; otherwise follow the longest prefix that does exist and return the first word that completes it.
    # EXAMPLE: Words 'cat', 'catnap', 'catnip' -> `autocorrect('catnar')` -> `'catnap'`; `autocorrect('cat')` -> `'cat'`
    # BIGO: O(K + M).
    def autocorrect(self, word):
        raise NotImplementedError
    # ==== END

    # ==== EX 17.9 | Delete a word | Stretch | class=Trie
    # PROMPT: Add `delete(word)` that removes the end marker and prunes nodes that no longer lead to any word. Return `True` if the word was present.
    # EXAMPLE: Words 'cat', 'catnip' -> delete 'catnip' -> 'cat' still found, the 'n-i-p' nodes are gone
    # BIGO: O(K).
    def delete(self, word):
        raise NotImplementedError
    # ==== END


# ==== EX 17.8 | Tries with values: ranked autocomplete | Practice | class=RankedTrie
# PROMPT: Build `RankedTrie(Trie)` whose `insert(word, popularity)` stores the popularity under `'*'`. Add `autocomplete(prefix, limit=3)` returning the most popular completions first.
# EXAMPLE: ('catnip', 9), ('cat', 5), ('catalog', 7) -> `autocomplete('cat', 2)` -> `['catnip', 'catalog']`
# BIGO: O(K + M + R log R) to collect and sort R matches.
class RankedTrie(Trie):
    def insert(self, word, popularity=0):
        raise NotImplementedError

    def _collect(self, node, word, out):
        raise NotImplementedError

    def autocomplete(self, prefix, limit=3):
        raise NotImplementedError
# ==== END
