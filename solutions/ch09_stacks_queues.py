"""Chapter 9: Stacks, queues and their constraints."""
from collections import deque


# ==== EX 9.1 | Stack | Core | class=Stack
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


# ==== EX 9.2 | Queue | Core | class=Queue
# PROMPT: Build `Queue` with `enqueue`, `dequeue`, `read` (front), `is_empty`, `__len__`. Use `collections.deque`, then explain why `list.pop(0)` would be a poor choice.
# EXAMPLE: enqueue 1, 2, 3 -> `dequeue()` is `1`, `read()` is `2`
# BIGO: O(1) each with a deque. `list.pop(0)` is O(N) because every element shifts left (see 1.11).
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


# ==== EX 9.3 | Bracket linter | Core
# PROMPT: Write `lint(code)` using your `Stack`. Return `None` if `()`, `[]`, `{}` are balanced, else a message naming the problem character.
# EXAMPLE: `'(var x = {y: [1, 2, 3]})'` -> `None`; `'(var x = 2;'` -> `'( has no closing brace'`; `'var x = 2)'` -> `') has no opening brace'`
# BIGO: O(N) time, O(N) space for the stack.
def lint(code):
    raise NotImplementedError
# ==== END


# ==== EX 9.4 | Reverse a string with a stack | Core
# PROMPT: Write `reverse_with_stack(s)` pushing every character and popping them back out.
# EXAMPLE: `'abcde'` -> `'edcba'`
# BIGO: O(N) time and space.
def reverse_with_stack(s):
    raise NotImplementedError
# ==== END


# ==== EX 9.5 | Print manager | Core | class=PrintManager
# PROMPT: Build `PrintManager` with `queue_job(document)` and `run()`, which prints jobs first-come-first-served and returns them in print order.
# EXAMPLE: queue `'First'`, `'Second'`, `'Third'` -> `run()` returns `['First', 'Second', 'Third']`
# BIGO: O(1) per job queued or printed.
class PrintManager:
    def __init__(self):
        raise NotImplementedError

    def queue_job(self, document):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError
# ==== END


# ==== EX 9.6 | Queue built from two stacks | Practice | class=StackQueue
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


# ==== EX 9.7 | Evaluate postfix (RPN) | Practice
# PROMPT: Write `eval_rpn(tokens)` for `+ - * /` (true division) using a stack.
# EXAMPLE: `['3', '4', '+', '2', '*']` -> `14`
# BIGO: O(N).
def eval_rpn(tokens):
    raise NotImplementedError
# ==== END


# ==== EX 9.8 | Undo and redo | Practice | class=Editor
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


# ==== EX 9.9 | Fixed-size circular queue | Stretch | class=CircularQueue
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
