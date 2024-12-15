import os

import networkx as nx

from plot_graph import plot_graph
from productions.p8.production8 import ProductionP8

view = os.environ.get("VIEW", False)


def base_example_graph() -> nx.Graph:
    G = nx.Graph()

    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),

        ('v:1.0:0.5', {'label': 'v', 'x': 1.0, 'y': 0.5, 'h': 1}),

        ('v:2.0:0.5', {'label': 'v', 'x': 2.0, 'y': 0.5, 'h': 0}),
        ('v:2.0:1.0', {'label': 'v', 'x': 2.0, 'y': 1.0, 'h': 0}),

        ('Q:0.5:0.5', {'label': 'Q', 'R': 0}),
        ('Q:1.5:0.75', {'label': 'Q', 'R': 1}),
    ])

    G.add_edges_from([
        ('v:0.0:0.0', 'v:1.0:0.0', {'label': 'E', 'B': 1}),
        ('v:1.0:0.0', 'v:1.0:1.0', {'label': 'E', 'B': 1}),
        ('v:1.0:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),
        ('v:0.0:1.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),

        ('v:1.0:0.5', 'v:1.0:1.0', {'label': 'E', 'B': 1}),
        ('v:1.0:0.0', 'v:1.0:0.5', {'label': 'E', 'B': 1}),

        ('Q:0.5:0.5', 'v:0.0:0.0'),
        ('Q:0.5:0.5', 'v:1.0:0.0'),
        ('Q:0.5:0.5', 'v:1.0:1.0'),
        ('Q:0.5:0.5', 'v:0.0:1.0'),

        ('Q:1.5:0.75', 'v:1.0:1.0'),
        ('Q:1.5:0.75', 'v:1.0:0.5'),
        ('Q:1.5:0.75', 'v:2.0:0.5'),
        ('Q:1.5:0.75', 'v:2.0:1.0'),
    ])

    return G


def test_base_example_p8():
    graph = base_example_graph()
    production = ProductionP8(graph)
    if view:
        plot_graph(graph, "TEST 1")

    # Verify if the production correctly identifies hyper edges
    result = production.extract_left_side()
    assert result is not None, "No suitable nodes found for applying the production"

    # Check initial conditions of the production
    assert graph.nodes['Q:0.5:0.5']['R'] == 0, "Node Q:0.5:0.5 should have R=0 before applying the production"
    assert graph.nodes['Q:1.5:0.75']['R'] == 1, "Node Q:1.5:0.75 should have R=1 before applying the production"
    assert graph.nodes['v:1.0:0.5']['h'] == 1, "Node v:1.0:0.5 should be a.py hanging node (h=1)"

    # Apply the production
    production.apply()
    if view:
        plot_graph(graph, "TEST 1 - AFTER PRODUCTION")

    # Check conditions after the production
    assert graph.nodes['Q:0.5:0.5']['R'] == 1, "Node Q:0.5:0.5 should have R=1 after applying the production"
    assert graph.nodes['Q:1.5:0.75']['R'] == 1, "Node Q:1.5:0.75 should still have R=1 after applying the production"
    assert graph.nodes['v:1.0:0.5']['h'] == 1, "Node v:1.0:0.5 should still be a.py hanging node (h=1)"
