from ch18_graphs import (Vertex, add_edge, bfs_traverse, count_components, dfs_search, dfs_traverse, dijkstra,
                         shortest_path, topological_order)


def make_people():
    alice, bob, candy, derek = (Vertex(n) for n in ('Alice', 'Bob', 'Candy', 'Derek'))
    alice.add_adjacent(bob)
    alice.add_adjacent(candy)
    bob.add_adjacent(derek)
    return alice, bob, candy, derek


def test_ex_18_1():
    g = {}
    add_edge(g, 'Alice', 'Bob')
    assert g == {'Alice': ['Bob'], 'Bob': ['Alice']}
    add_edge(g, 'Alice', 'Bob')
    add_edge(g, 'Bob', 'Cy', directed=True)
    assert g == {'Alice': ['Bob'], 'Bob': ['Alice', 'Cy'], 'Cy': []}


def test_ex_18_2():
    alice, bob, candy, derek = make_people()
    assert alice in bob.adjacent and bob in alice.adjacent and derek in bob.adjacent
    alice.add_adjacent(bob)
    assert alice.adjacent.count(bob) == 1


def test_ex_18_3():
    alice, *_ = make_people()
    assert dfs_traverse(alice) == ['Alice', 'Bob', 'Derek', 'Candy']


def test_ex_18_4():
    alice, bob, candy, derek = make_people()
    assert dfs_search(alice, 'Derek') is derek and dfs_search(alice, 'Zed') is None


def test_ex_18_5():
    alice, *_ = make_people()
    assert bfs_traverse(alice) == ['Alice', 'Bob', 'Candy', 'Derek']


def test_ex_18_6():
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C', 'E'], 'E': ['D']}
    assert shortest_path(graph, 'A', 'E') == ['A', 'B', 'D', 'E'] and shortest_path(graph, 'A', 'Z') is None


def test_ex_18_7():
    assert count_components({'a': ['b'], 'b': ['a'], 'c': [], 'd': ['e'], 'e': ['d']}) == 3


def test_ex_18_8():
    routes = {'Atlanta': {'Boston': 100, 'Denver': 160}, 'Boston': {'Chicago': 120, 'Denver': 180},
              'Chicago': {'El Paso': 80}, 'Denver': {'Chicago': 40, 'El Paso': 140}, 'El Paso': {'Boston': 100}}
    assert dijkstra(routes, 'Atlanta', 'El Paso') == (280, ['Atlanta', 'Denver', 'Chicago', 'El Paso'])
    assert dijkstra(routes, 'Atlanta', 'Atlanta') == (0, ['Atlanta'])
    assert dijkstra(routes, 'El Paso', 'Atlanta') == (None, [])


def test_ex_18_9():
    deps = {'wake': ['shower', 'coffee'], 'shower': ['dress'], 'coffee': ['dress'], 'dress': []}
    assert topological_order(deps) == ['wake', 'shower', 'coffee', 'dress']
    assert topological_order({'a': ['b'], 'b': ['a']}) is None
