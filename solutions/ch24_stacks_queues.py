"""Chapter 24: Stacks and queues."""
from collections import deque


# ==== EX 24.1 | Stack | Core | class=Stack
# PROMPT: Build `Stack` on a Python list, exposing only `push`, `pop`, `read` (peek), `is_empty` and `__len__`. `pop` and `read` return `None` when empty.
# EXAMPLE: push 1, 2, 3 -> `read()` is `3`, `pop()` is `3`, `read()` is `2`
# BIGO: O(1) for every operation. The end of a list is the cheap end.
# NOTE: A stack is an abstract data type: the constraint (last in, first out) matters, not the list underneath.
class Stack:
    def __init__(self):
        raise NotImplementedError

    def push(self, value):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def read(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError
# ==== END


# ==== EX 24.2 | Queue | Core | class=Queue
# PROMPT: Build `Queue` with `enqueue`, `dequeue`, `read` (front), `is_empty`, `__len__`. Use `collections.deque`, then explain why `list.pop(0)` would be a poor choice.
# EXAMPLE: enqueue 1, 2, 3 -> `dequeue()` is `1`, `read()` is `2`
# BIGO: O(1) each with a deque. `list.pop(0)` is O(N) because every element shifts left (see 21.11).
class Queue:
    def __init__(self):
        raise NotImplementedError

    def enqueue(self, value):
        raise NotImplementedError

    def dequeue(self):
        raise NotImplementedError

    def read(self):
        raise NotImplementedError

    def is_empty(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError
# ==== END


# ==== EX 24.3 | Do the tags nest? | Core
# PROMPT: Write `tags_balanced(markup)` using your `Stack`. Tags are `<name>` and `</name>` with letters only and no attributes; text between tags is ignored. Return `True` when every tag closes, in the reverse order it opened.
# EXAMPLE: `'<p><b>hi</b></p>'` -> `True`; `'<p><b></p></b>'` -> `False`
# BIGO: O(N) time, O(N) space for the stack.
def tags_balanced(markup):
    raise NotImplementedError
# ==== END


# ==== EX 24.4 | Simplify a file path | Core
# PROMPT: Write `simplify_path(path)` for an absolute path: drop empty parts and `.`, let `..` remove the folder before it (if any), and return the canonical path. Use your `Stack` for the folders.
# EXAMPLE: `'/a/./b/../c/'` -> `'/a/c'`; `'/../'` -> `'/'`
# BIGO: O(N) time and space.
def simplify_path(path):
    raise NotImplementedError
# ==== END


# ==== EX 24.5 | Round-robin turns | Core
# PROMPT: Write `round_robin(names, times, slice_)` using your `Queue`: job `names[i]` needs `times[i]` units of work. The front job runs for up to `slice_` units; if it still has work left it goes to the back. Return the names in the order the jobs finish.
# EXAMPLE: `['a', 'b', 'c'], [3, 1, 2], 1` -> `['b', 'c', 'a']`
# BIGO: O(T / s + N) queue operations for total work T, slice s and N jobs; each one is O(1).
def round_robin(names, times, slice_):
    raise NotImplementedError
# ==== END


# ==== EX 24.6 | Queue built from two stacks | Practice | class=StackQueue
# PROMPT: Build `StackQueue` with `enqueue` and `dequeue` using only two `Stack` objects.
# EXAMPLE: enqueue 1, 2; dequeue -> `1`; enqueue 3; dequeue -> `2`, dequeue -> `3`
# BIGO: O(1) amortized: each element is moved from the inbox to the outbox at most once.
class StackQueue:
    def __init__(self):
        raise NotImplementedError

    def enqueue(self, value):
        raise NotImplementedError

    def dequeue(self):
        raise NotImplementedError
# ==== END


# ==== EX 24.7 | Evaluate postfix (RPN) | Practice
# PROMPT: Write `eval_rpn(tokens)` for `+ - * /` (true division) using a stack.
# EXAMPLE: `['3', '4', '+', '2', '*']` -> `14`
# BIGO: O(N).
def eval_rpn(tokens):
    raise NotImplementedError
# ==== END


# ==== EX 24.8 | Undo and redo | Practice | class=Editor
# PROMPT: Build `Editor` with `type(text)`, `undo()`, `redo()` and a `text` attribute. Use one stack of past states and one of undone states; new typing clears redo.
# EXAMPLE: type 'a', type 'b', undo -> `'a'`; redo -> `'ab'`
# BIGO: O(1) per operation (plus the cost of building the new string).
class Editor:
    def __init__(self):
        raise NotImplementedError

    def type(self, chars):
        raise NotImplementedError

    def undo(self):
        raise NotImplementedError

    def redo(self):
        raise NotImplementedError
# ==== END


# ==== EX 24.9 | Fixed-size circular queue | Stretch | class=CircularQueue
# PROMPT: Build `CircularQueue(capacity)` on a fixed list with `head` and `size`, so neither `enqueue` nor `dequeue` shifts anything. `enqueue` returns `False` when full.
# EXAMPLE: capacity 3: enqueue 1, 2, 3 -> 4th returns `False`; dequeue -> `1`; enqueue 4 succeeds and wraps to slot 0
# BIGO: O(1) for both, with no shifting, because the index wraps with `% capacity`.
class CircularQueue:
    def __init__(self, capacity):
        raise NotImplementedError

    def enqueue(self, value):
        raise NotImplementedError

    def dequeue(self):
        raise NotImplementedError
# ==== END
