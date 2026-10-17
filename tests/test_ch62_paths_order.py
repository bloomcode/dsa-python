from ch62_paths_order import dijkstra, shortest_path, topological_order


def test_ex_62_1():
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'D'], 'D': ['B', 'C', 'E'], 'E': ['D']}
    assert shortest_path(graph, 'A', 'E') == ['A', 'B', 'D', 'E'] and shortest_path(graph, 'A', 'Z') is None


def test_ex_62_2():
    routes = {'Ames': {'Bern': 4, 'Cork': 2}, 'Bern': {'Dover': 5}, 'Cork': {'Bern': 1, 'Dover': 8, 'Eden': 10},
              'Dover': {'Eden': 2}, 'Eden': {}}
    assert dijkstra(routes, 'Ames', 'Eden') == (10, ['Ames', 'Cork', 'Bern', 'Dover', 'Eden'])
    assert dijkstra(routes, 'Ames', 'Ames') == (0, ['Ames'])
    assert dijkstra(routes, 'Ames', 'Dover') == (8, ['Ames', 'Cork', 'Bern', 'Dover'])
    assert dijkstra(routes, 'Eden', 'Ames') == (None, [])


def test_ex_62_3():
    deps = {'wake': ['shower', 'coffee'], 'shower': ['dress'], 'coffee': ['dress'], 'dress': []}
    assert topological_order(deps) == ['wake', 'shower', 'coffee', 'dress']
    assert topological_order({'a': ['b'], 'b': ['a']}) is None
