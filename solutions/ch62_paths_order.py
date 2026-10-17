"""Chapter 62: Shortest paths and ordering."""
import heapq
from collections import deque


# ==== EX 62.1 | Shortest path, unweighted | Core
# PROMPT: Write `shortest_path(graph, start, end)` on a dict graph using BFS and a `previous` map, returning the list of vertices or `None`.
# EXAMPLE: `{'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C', 'E'], 'E': ['D']}`, A to E -> `['A', 'B', 'D', 'E']`
# BIGO: O(V + E). The first time BFS reaches a vertex is along a fewest-edges path.
def shortest_path(graph, start, end):
    raise NotImplementedError
# ==== END


# ==== EX 62.2 | Fastest route by travel time | Core
# PROMPT: Write `dijkstra(routes, start, end)` for `routes = {town: {neighbour: minutes}}`. Return `(total_cost, path)` or `(None, [])`. Use `heapq` to always visit the nearest known unvisited town next.
# EXAMPLE: `routes = {'Ames': {'Bern': 4, 'Cork': 2}, 'Bern': {'Dover': 5}, 'Cork': {'Bern': 1, 'Dover': 8, 'Eden': 10}, 'Dover': {'Eden': 2}}` -> Ames to Eden is `(10, ['Ames', 'Cork', 'Bern', 'Dover', 'Eden'])`
# BIGO: O((V + E) log V) with a heap. Scanning an array for the cheapest unvisited city instead is O(V^2).
# NOTE: Dijkstra requires non-negative weights.
def dijkstra(routes, start, end):
    raise NotImplementedError
# ==== END


# ==== EX 62.3 | Topological order of tasks | Stretch
# PROMPT: Write `topological_order(deps)` for a directed graph `{task: [tasks that depend on it]}` using Kahn's algorithm (repeatedly take tasks with no remaining prerequisites). Return `None` if there is a cycle.
# EXAMPLE: `{'wake': ['shower', 'coffee'], 'shower': ['dress'], 'coffee': ['dress'], 'dress': []}` -> `['wake', 'shower', 'coffee', 'dress']`
# BIGO: O(V + E).
def topological_order(deps):
    raise NotImplementedError
# ==== END
