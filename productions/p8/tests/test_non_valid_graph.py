import os

import networkx as nx

from plot_graph import plot_graph
from productions.p8.production8 import ProductionP8

view = os.environ.get("VIEW", False)


def non_valid_graph() -> nx.Graph:
    G = nx.Graph()

    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),

        ('v:2.0:1.0', {'label': 'v', 'x': 2.0, 'y': 1.0, 'h': 0}),
        ('v:2.0:2.0', {'label': 'v', 'x': 2.0, 'y': 2.0, 'h': 0}),
        ('v:1.0:2.0', {'label': 'v', 'x': 1.0, 'y': 2.0, 'h': 0}),

        ('Q:0.5:0.5', {'label': 'Q', 'R': 0}),
        ('Q:1.5:1.5', {'label': 'Q', 'R': 1}),
    ])

    G.add_edges_from([
        ('v:0.0:0.0', 'v:1.0:0.0', {'label': 'E', 'B': 1}),
        ('v:1.0:0.0', 'v:1.0:1.0', {'label': 'E', 'B': 1}),
        ('v:1.0:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),
        ('v:0.0:1.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),

        ('Q:0.5:0.5', 'v:0.0:0.0'),
        ('Q:0.5:0.5', 'v:1.0:0.0'),
        ('Q:0.5:0.5', 'v:1.0:1.0'),
        ('Q:0.5:0.5', 'v:0.0:1.0'),

        ('Q:1.5:1.5', 'v:1.0:1.0'),
        ('Q:1.5:1.5', 'v:2.0:2.0'),
        ('Q:1.5:1.5', 'v:2.0:1.0'),
        ('Q:1.5:1.5', 'v:1.0:2.0'),
    ])

    return G


def test_non_valid_graph_p8():
    # Preparing the non-valid graph
    graph = non_valid_graph()
    production = ProductionP8(graph)
    if view:
        plot_graph(graph, "TEST 2")

    # Attempting to find the left side of the production should fail
    result = production.extract_left_side()
    assert result is None, "The production should not find matching nodes in a.py non-compliant graph"

    # Check initial conditions of the production
    assert graph.nodes['Q:0.5:0.5']['R'] == 0, "Node Q:0.5:0.5 should have R=0 before applying the production"
    assert graph.nodes['Q:1.5:1.5']['R'] == 1, "Node Q:1.5:0.75 should have R=1 before applying the production"

    # Apply the production
    production.apply()
    if view:
        plot_graph(graph, "TEST 2 - AFTER PRODUCTION")

    # Check conditions after the production
    assert graph.nodes['Q:0.5:0.5']['R'] == 0, "Node Q:0.5:0.5 should have R=0 after applying the production"
    assert graph.nodes['Q:1.5:1.5']['R'] == 1, "Node Q:1.5:0.75 should still have R=1 after applying the production"
