"""Chapter 18: Graphs: traversal and cheapest paths."""
import heapq
from collections import deque


# ==== EX 18.1 | Adjacency-list graph with a hash map | Core
# PROMPT: Write `add_edge(graph, a, b, directed=False)` for a graph stored as `{vertex: [neighbours]}`. Add missing vertices automatically and avoid duplicate edges.
# EXAMPLE: `g = {}; add_edge(g, 'Alice', 'Bob')` -> `{'Alice': ['Bob'], 'Bob': ['Alice']}`
# BIGO: O(D) for the duplicate check, where D is the vertex's degree. A set of neighbours would make it O(1).
def add_edge(graph, a, b, directed=False):
    raise NotImplementedError
# ==== END


# ==== EX 18.2 | Object-oriented vertex | Core | class=Vertex
# PROMPT: Create `Vertex(value)` with an `adjacent` list and `add_adjacent(vertex)` that links both ways (friendship is mutual) without recursing forever.
# EXAMPLE: `alice.add_adjacent(bob)` -> bob is in alice.adjacent and alice is in bob.adjacent
# BIGO: O(D) per link because of the membership check.
class Vertex:
    def __init__(self, value):
        raise NotImplementedError

    def add_adjacent(self, vertex):
        raise NotImplementedError
# ==== END


# ==== EX 18.3 | Depth-first traversal | Core
# PROMPT: Write `dfs_traverse(vertex, visited=None)` returning vertex values in visit order. Mark each vertex visited before recursing into its neighbours.
# EXAMPLE: Alice-Bob, Alice-Candy, Bob-Derek -> `['Alice', 'Bob', 'Derek', 'Candy']`
# BIGO: O(V + E). Without the visited set, a cycle would loop forever.
def dfs_traverse(vertex, visited=None):
    raise NotImplementedError
# ==== END


# ==== EX 18.4 | Depth-first search | Core
# PROMPT: Write `dfs_search(vertex, target_value, visited=None)` returning the matching `Vertex` or `None`.
# EXAMPLE: From Alice, search 'Derek' -> the Derek vertex
# BIGO: O(V + E) worst case.
def dfs_search(vertex, target_value, visited=None):
    raise NotImplementedError
# ==== END


# ==== EX 18.5 | Breadth-first traversal | Core
# PROMPT: Write `bfs_traverse(start)` using a queue: mark the start visited, then repeatedly dequeue a vertex and enqueue its unvisited neighbours.
# EXAMPLE: Same graph as 18.3 -> `['Alice', 'Bob', 'Candy', 'Derek']`
# BIGO: O(V + E).
# NOTE: BFS spreads out in rings, so it finds close vertices first; DFS dives deep first.
def bfs_traverse(start):
    raise NotImplementedError
# ==== END


# ==== EX 18.6 | Shortest path, unweighted | Core
# PROMPT: Write `shortest_path(graph, start, end)` on a dict graph using BFS and a `previous` map, returning the list of vertices or `None`.
# EXAMPLE: `{'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C', 'E'], 'E': ['D']}`, A to E -> `['A', 'B', 'D', 'E']`
# BIGO: O(V + E). The first time BFS reaches a vertex is along a fewest-edges path.
def shortest_path(graph, start, end):
    raise NotImplementedError
# ==== END


# ==== EX 18.7 | Count connected groups | Practice
# PROMPT: Write `count_components(graph)` returning how many separate groups an undirected dict graph has.
# EXAMPLE: `{'a': ['b'], 'b': ['a'], 'c': [], 'd': ['e'], 'e': ['d']}` -> `3`
# BIGO: O(V + E): each vertex is explored once across all searches.
def count_components(graph):
    raise NotImplementedError
# ==== END


# ==== EX 18.8 | Dijkstra's algorithm: cheapest flight | Core
# PROMPT: Write `dijkstra(routes, start, end)` for `routes = {city: {neighbour: price}}`. Return `(total_cost, path)` or `(None, [])`. Use `heapq` to always visit the cheapest known unvisited city next.
# EXAMPLE: Atlanta->Boston 100, Atlanta->Denver 160, Boston->Chicago 120, Boston->Denver 180, Chicago->El Paso 80, Denver->Chicago 40, Denver->El Paso 140 -> Atlanta to El Paso is `(280, ['Atlanta', 'Denver', 'Chicago', 'El Paso'])`
# BIGO: O((V + E) log V) with a heap. Scanning an array for the cheapest unvisited city instead is O(V^2).
# NOTE: Dijkstra requires non-negative weights.
def dijkstra(routes, start, end):
    raise NotImplementedError
# ==== END


# ==== EX 18.9 | Topological order of tasks | Stretch
# PROMPT: Write `topological_order(deps)` for a directed graph `{task: [tasks that depend on it]}` using Kahn's algorithm (repeatedly take tasks with no remaining prerequisites). Return `None` if there is a cycle.
# EXAMPLE: `{'wake': ['shower', 'coffee'], 'shower': ['dress'], 'coffee': ['dress'], 'dress': []}` -> `['wake', 'shower', 'coffee', 'dress']`
# BIGO: O(V + E).
def topological_order(deps):
    raise NotImplementedError
# ==== END
