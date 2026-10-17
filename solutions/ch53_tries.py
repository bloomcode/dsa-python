"""Chapter 53: Tries."""


# ==== EX 53.1 | Trie node and insertion | Core | class=Trie
# PROMPT: Create `TrieNode` with a `children` dict and `Trie` with a `root`. Write `insert(word)` that walks or creates one child per character, then adds a `'*'` child to mark the end of the word.
# EXAMPLE: insert 'pin', 'pit' -> root has one child `'p'`, whose `'i'` child has children `'n'` and `'t'`
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

    # ==== EX 53.2 | Search a prefix | Core | class=Trie
    # PROMPT: Add `search(prefix)` returning the node where the prefix ends, or `None` if it is not in the trie.
    # EXAMPLE: After 'pin' -> `search('pi')` is a node; `search('po')` is `None`
    # BIGO: O(K).
    def search(self, prefix):
        raise NotImplementedError
    # ==== END

    # ==== EX 53.3 | Is it a whole word? | Core | class=Trie
    # PROMPT: Add `contains_word(word)`: the prefix must exist and its node must have a `'*'` child.
    # EXAMPLE: After 'pin' -> `contains_word('pin')` is `True`, `contains_word('pi')` is `False`
    # BIGO: O(K).
    def contains_word(self, word):
        raise NotImplementedError
    # ==== END

    # ==== EX 53.4 | Collect every word | Core | class=Trie
    # PROMPT: Add `collect_all_words(node=None, word='', words=None)` that recursively gathers every word below `node` (the root by default).
    # EXAMPLE: After 'pin', 'pit', 'sun' -> `['pin', 'pit', 'sun']` (insertion order)
    # BIGO: O(M) for M nodes beneath the starting node.
    def collect_all_words(self, node=None, word="", words=None):
        raise NotImplementedError
    # ==== END

    # ==== EX 53.5 | Autocomplete | Core | class=Trie
    # PROMPT: Add `autocomplete(prefix)`: search to the prefix's node, collect the words below it and prepend the prefix.
    # EXAMPLE: Words 'pin', 'pinch', 'pit', 'sun' -> `autocomplete('pin')` -> `['pin', 'pinch']`
    # BIGO: O(K + M): reach the prefix, then visit only the matching subtree.
    def autocomplete(self, prefix):
        raise NotImplementedError
    # ==== END

    # ==== EX 53.6 | Print every key | Practice | class=Trie
    # PROMPT: Add `all_keys()` returning every character stored in the trie (excluding `'*'`), depth first.
    # EXAMPLE: After 'pie', 'pin' -> `['p', 'i', 'e', 'n']`
    # BIGO: O(M) nodes.
    def all_keys(self, node=None, keys=None):
        raise NotImplementedError
    # ==== END

    # ==== EX 53.7 | Longest prefix every word shares | Practice | class=Trie
    # PROMPT: Add `longest_common_prefix()`: walk down from the root while the current node has exactly one child and no word ends there, collecting the characters. Return `''` for an empty trie.
    # EXAMPLE: Words 'pine', 'pint', 'pinto' -> `'pin'`; words 'pin', 'pinch' -> `'pin'`
    # BIGO: O(P) where P is the length of the shared prefix: only one path is ever walked.
    def longest_common_prefix(self):
        raise NotImplementedError
    # ==== END

    # ==== EX 53.9 | Delete a word | Stretch | class=Trie
    # PROMPT: Add `delete(word)` that removes the end marker and prunes nodes that no longer lead to any word. Return `True` if the word was present.
    # EXAMPLE: Words 'pin', 'pinch' -> delete 'pinch' -> 'pin' still found, the 'c-h' nodes are gone
    # BIGO: O(K).
    def delete(self, word):
        raise NotImplementedError
    # ==== END


# ==== EX 53.8 | Tries with values: ranked autocomplete | Practice | class=RankedTrie
# PROMPT: Build `RankedTrie(Trie)` whose `insert(word, popularity)` stores the popularity under `'*'`. Add `autocomplete(prefix, limit=3)` returning the most popular completions first.
# EXAMPLE: ('pinch', 9), ('pin', 5), ('pinball', 7) -> `autocomplete('pin', 2)` -> `['pinch', 'pinball']`
# BIGO: O(K + M + R log R) to collect and sort R matches.
class RankedTrie(Trie):
    def insert(self, word, popularity=0):
        raise NotImplementedError

    def _collect(self, node, word, out):
        raise NotImplementedError

    def autocomplete(self, prefix, limit=3):
        raise NotImplementedError
# ==== END
