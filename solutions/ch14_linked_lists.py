"""Chapter 14: Linked lists, singly and doubly."""


# ==== EX 14.1 | Node and LinkedList skeleton | Core | class=LinkedList
# PROMPT: Create `Node(data)` with `data` and `next`, and `LinkedList` with `head`. Add `__len__` and `to_list()` that walk the chain, plus a `from_list(values)` class method for tests.
# EXAMPLE: `LinkedList.from_list([1, 2, 3]).to_list()` -> `[1, 2, 3]`
# BIGO: `__len__` and `to_list` are O(N): there is no length stored, so every node must be visited.
# NOTE: Nodes can live anywhere in memory; each one only knows where the next one is. That is what makes reading slow and insertion at the head fast.
class Node:
    def __init__(self, data, next_node=None):
        raise NotImplementedError


class LinkedList:
    def __init__(self, head=None):
        raise NotImplementedError

    @classmethod
    def from_list(cls, values):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError

    def to_list(self):
        raise NotImplementedError
# ==== END

    # ==== EX 14.2 | Read by index | Core | class=LinkedList
    # PROMPT: Add `read(index)`: follow `next` links `index` times. Return `None` if the list is too short.
    # EXAMPLE: `[10, 20, 30]` -> `read(2)` is `30`; `read(5)` is `None`
    # BIGO: O(N). An array reads in O(1); this is the linked list's biggest cost.
    def read(self, index):
        raise NotImplementedError
    # ==== END

    # ==== EX 14.3 | Search for a value | Core | class=LinkedList
    # PROMPT: Add `index_of(value)` returning the position of the first match, or `None`.
    # EXAMPLE: `[10, 20, 30]` -> `index_of(20)` is `1`
    # BIGO: O(N), the same as linear search in an array.
    def index_of(self, value):
        raise NotImplementedError
    # ==== END

    # ==== EX 14.4 | Insert at the start | Core | class=LinkedList
    # PROMPT: Add `insert_at_start(value)`: the new node points at the old head and becomes the head.
    # EXAMPLE: `[2, 3]` -> `insert_at_start(1)` -> `[1, 2, 3]`
    # BIGO: O(1). The array's worst case is the linked list's best case.
    def insert_at_start(self, value):
        raise NotImplementedError
    # ==== END

    # ==== EX 14.5 | Insert at the end | Core | class=LinkedList
    # PROMPT: Add `insert_at_end(value)`: walk to the last node and attach the new one. Handle the empty list.
    # EXAMPLE: `[1, 2]` -> `insert_at_end(3)` -> `[1, 2, 3]`
    # BIGO: O(N) without a tail pointer (see 14.15 for O(1)).
    def insert_at_end(self, value):
        raise NotImplementedError
    # ==== END

    # ==== EX 14.6 | Insert at an index | Core | class=LinkedList
    # PROMPT: Add `insert_at(index, value)`: walk to the node just before `index`, then rewire two links. Raise `IndexError` if `index` is past the end.
    # EXAMPLE: `[1, 2, 4]` -> `insert_at(2, 3)` -> `[1, 2, 3, 4]`
    # BIGO: O(N) to find the spot, then O(1) to insert. No shifting, unlike an array.
    # NOTE: Set `new_node.next` before changing `prev.next`, or the rest of the list is lost.
    def insert_at(self, index, value):
        raise NotImplementedError
    # ==== END

    # ==== EX 14.7 | Delete at the start | Core | class=LinkedList
    # PROMPT: Add `delete_at_start()` returning the removed value (or `None` if empty): move `head` to `head.next`.
    # EXAMPLE: `[1, 2, 3]` -> returns `1`, leaves `[2, 3]`
    # BIGO: O(1). Arrays need O(N) here.
    def delete_at_start(self):
        raise NotImplementedError
    # ==== END

    # ==== EX 14.8 | Delete at the end | Core | class=LinkedList
    # PROMPT: Add `delete_at_end()` returning the removed value: find the second-to-last node and cut its link. Handle 0 and 1 nodes.
    # EXAMPLE: `[1, 2, 3]` -> returns `3`, leaves `[1, 2]`
    # BIGO: O(N) in a singly linked list, because you need the node before the last one.
    def delete_at_end(self):
        raise NotImplementedError
    # ==== END

    # ==== EX 14.9 | Delete at an index | Core | class=LinkedList
    # PROMPT: Add `delete_at(index)` returning the removed value: point the previous node's `next` past the doomed node. Raise `IndexError` if out of range.
    # EXAMPLE: `[1, 2, 9, 3]` -> `delete_at(2)` returns `9`, leaves `[1, 2, 3]`
    # BIGO: O(N) to reach it, O(1) to unlink.
    def delete_at(self, index):
        raise NotImplementedError
    # ==== END

    # ==== EX 14.10 | Delete by value | Core | class=LinkedList
    # PROMPT: Add `delete_value(value)` that removes the first matching node and returns `True`, or `False`.
    # EXAMPLE: `[4, 5, 4]` -> `delete_value(4)` -> `[5, 4]`
    # BIGO: O(N).
    def delete_value(self, value):
        raise NotImplementedError
    # ==== END

    # ==== EX 14.11 | Last value and middle value | Practice | class=LinkedList
    # PROMPT: Add `last()` and `middle()`. For `middle`, move a slow pointer one step and a fast pointer two steps; when fast reaches the end, slow is in the middle (second middle for an even count).
    # EXAMPLE: `[1, 2, 3, 4, 5]` -> `last()` is `5`, `middle()` is `3`; `[1, 2, 3, 4]` -> `middle()` is `3`
    # BIGO: O(N) each, one pass, O(1) space.
    def last(self):
        raise NotImplementedError

    def middle(self):
        raise NotImplementedError
    # ==== END

    # ==== EX 14.12 | Reverse in place | Core | class=LinkedList
    # PROMPT: Add `reverse()` that flips every `next` link using `previous`, `current` and `next` variables.
    # EXAMPLE: `[1, 2, 3]` -> `[3, 2, 1]`
    # BIGO: O(N) time, O(1) space.
    def reverse(self):
        raise NotImplementedError
    # ==== END

    # ==== EX 14.14 | Detect a cycle | Stretch | class=LinkedList
    # PROMPT: Add `has_cycle()` using Floyd's slow/fast pointers: if they ever meet, the list loops.
    # EXAMPLE: A list whose last node points back to its second node -> `True`
    # BIGO: O(N) time, O(1) space (a set of visited nodes would be O(N) space).
    def has_cycle(self):
        raise NotImplementedError
    # ==== END


# ==== EX 14.13 | Delete a node given only that node | Practice
# PROMPT: Write `delete_node(node)` that removes `node` from its list when you have no access to the head. (It is never the last node.)
# EXAMPLE: In `a -> b -> c -> d`, `delete_node(b)` leaves `a -> c -> d`
# BIGO: O(1). Copy the next node's data in, then skip the next node.
def delete_node(node):
    raise NotImplementedError
# ==== END


# ==== EX 14.15 | Doubly linked list | Core | class=DoublyLinkedList
# PROMPT: Build `DoublyLinkedList` with `head` and `tail` and nodes holding `prev` and `next`. Implement `insert_at_start`, `insert_at_end`, `delete_at_start`, `delete_at_end`, `to_list()` and `to_list_reversed()` (walk back from the tail).
# EXAMPLE: insert_at_end 2, insert_at_start 1, insert_at_end 3 -> `[1, 2, 3]`; reversed `[3, 2, 1]`
# BIGO: O(1) at both ends, because the tail pointer and `prev` links remove the walk.
class DNode:
    def __init__(self, data):
        raise NotImplementedError


class DoublyLinkedList:
    def __init__(self):
        raise NotImplementedError

    def insert_at_start(self, value):
        raise NotImplementedError

    def insert_at_end(self, value):
        raise NotImplementedError

    def delete_at_start(self):
        raise NotImplementedError

    def delete_at_end(self):
        raise NotImplementedError

    def to_list(self):
        raise NotImplementedError

    def to_list_reversed(self):
        raise NotImplementedError
# ==== END


# ==== EX 14.16 | Queue on a doubly linked list | Core | class=LinkedQueue
# PROMPT: Build `LinkedQueue` with `enqueue`, `dequeue` and `read` on top of your `DoublyLinkedList`.
# EXAMPLE: enqueue 1, 2, 3 -> dequeue `1`, read `2`
# BIGO: O(1) for every operation: insert at the tail, remove from the head.
class LinkedQueue:
    def __init__(self):
        raise NotImplementedError

    def enqueue(self, value):
        raise NotImplementedError

    def dequeue(self):
        raise NotImplementedError

    def read(self):
        raise NotImplementedError
# ==== END
