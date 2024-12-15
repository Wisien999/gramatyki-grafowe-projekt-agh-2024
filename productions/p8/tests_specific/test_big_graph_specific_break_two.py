import os

import networkx as nx

from plot_graph import plot_graph
from productions.p8.production8 import ProductionP8

view = os.environ.get("VIEW", False)


def big_graph_specific() -> nx.Graph:
    G = nx.Graph()

    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),

        ('v:2.0:1.0', {'label': 'v', 'x': 2.0, 'y': 1.0, 'h': 0}),
        ('v:2.0:2.0', {'label': 'v', 'x': 2.0, 'y': 2.0, 'h': 0}),
        ('v:1.0:2.0', {'label': 'v', 'x': 1.0, 'y': 2.0, 'h': 0}),

        ('v:1.0:0.5', {'label': 'v', 'x': 1.0, 'y': 0.5, 'h': 1}),
        ('v:1.5:0.5', {'label': 'v', 'x': 1.5, 'y': 0.5, 'h': 0}),
        ('v:1.5:1.0', {'label': 'v', 'x': 1.5, 'y': 1.0, 'h': 1}),

        ('Q:0.5:0.5', {'label': 'Q', 'R': 0}),
        ('Q:1.5:1.5', {'label': 'Q', 'R': 0}),
        ('Q:2.5:0.5', {'label': 'Q', 'R': 0}),

        ('Q:1.25:0.75', {'label': 'Q', 'R': 1}),
        ('Q:1.25:0.25', {'label': 'Q', 'R': 1}),
        ('Q:1.75:0.25', {'label': 'Q', 'R': 1}),
        ('Q:1.75:0.75', {'label': 'Q', 'R': 1}),


        ('v:1.5:0.0', {'label': 'v', 'x': 1.5, 'y': 0.0, 'h': 0}),
        ('v:1.5:0.0', {'label': 'v', 'x': 1.5, 'y': 0.0, 'h': 0}),
        ('v:1.5:0.0', {'label': 'v', 'x': 1.5, 'y': 0.0, 'h': 0}),

        ('v:2.0:0.0', {'label': 'v', 'x': 2.0, 'y': 0.0, 'h': 0}),
        ('v:2.0:0.5', {'label': 'v', 'x': 2.0, 'y': 0.5, 'h': 1}),

        ('v:3.0:0.0', {'label': 'v', 'x': 3.0, 'y': 0.0, 'h': 0}),
        ('v:3.0:1.0', {'label': 'v', 'x': 3.0, 'y': 1.0, 'h': 0}),
    ])

    G.add_edges_from([
        ('v:0.0:0.0', 'v:1.0:0.0', {'label': 'E', 'B': 1}),
        ('v:1.0:0.0', 'v:1.0:1.0', {'label': 'E', 'B': 1}),
        ('v:1.0:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),
        ('v:0.0:1.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),

        ('v:1.0:1.0', 'v:2.0:1.0', {'label': 'E', 'B': 1}),
        ('v:2.0:1.0', 'v:2.0:2.0', {'label': 'E', 'B': 1}),
        ('v:2.0:2.0', 'v:1.0:2.0', {'label': 'E', 'B': 1}),
        ('v:1.0:2.0', 'v:1.0:1.0', {'label': 'E', 'B': 1}),

        ('Q:0.5:0.5', 'v:0.0:0.0'),
        ('Q:0.5:0.5', 'v:1.0:0.0'),
        ('Q:0.5:0.5', 'v:1.0:1.0'),
        ('Q:0.5:0.5', 'v:0.0:1.0'),

        ('Q:1.5:1.5', 'v:1.0:1.0'),
        ('Q:1.5:1.5', 'v:2.0:2.0'),
        ('Q:1.5:1.5', 'v:2.0:1.0'),
        ('Q:1.5:1.5', 'v:1.0:2.0'),

        ('Q:1.25:0.75', 'v:1.0:1.0'),
        ('Q:1.25:0.75', 'v:1.0:0.5'),
        ('Q:1.25:0.75', 'v:1.5:0.5'),
        ('Q:1.25:0.75', 'v:1.5:1.0'),

        ('v:1.0:1.0', 'v:1.5:1.0', {'label': 'E', 'B': 0}),
        ('v:1.0:1.0', 'v:1.0:0.5', {'label': 'E', 'B': 0}),

        ('v:1.5:0.5', 'v:1.0:0.5', {'label': 'E', 'B': 0}),
        ('v:1.5:0.5', 'v:1.5:1.0', {'label': 'E', 'B': 0}),

        ('v:2.0:1.0', 'v:1.5:1.0', {'label': 'E', 'B': 0}),
        ('v:1.0:1.0', 'v:1.5:1.0', {'label': 'E', 'B': 0}),

        ('v:1.0:0.0', 'v:1.0:0.5', {'label': 'E', 'B': 0}),

        ('v:1.0:0.0', 'v:1.5:0.0', {'label': 'E', 'B': 0}),
        ('v:1.5:0.5', 'v:1.5:0.0', {'label': 'E', 'B': 0}),

        ('Q:1.25:0.25', 'v:1.0:0.0'),
        ('Q:1.25:0.25', 'v:1.0:0.5'),
        ('Q:1.25:0.25', 'v:1.5:0.5'),
        ('Q:1.25:0.25', 'v:1.5:0.0'),

        ('Q:1.75:0.25', 'v:2.0:0.0'),
        ('Q:1.75:0.25', 'v:2.0:0.5'),
        ('Q:1.75:0.25', 'v:1.5:0.5'),
        ('Q:1.75:0.25', 'v:1.5:0.0'),

        ('Q:1.75:0.75', 'v:2.0:1.0'),
        ('Q:1.75:0.75', 'v:2.0:0.5'),
        ('Q:1.75:0.75', 'v:1.5:0.5'),
        ('Q:1.75:0.75', 'v:1.5:1.0'),

        ('v:2.0:0.0', 'v:2.0:0.5', {'label': 'E', 'B': 0}),
        ('v:2.0:0.0', 'v:2.0:0.5', {'label': 'E', 'B': 0}),
        ('v:2.0:0.5', 'v:2.0:1.0', {'label': 'E', 'B': 0}),

        ('v:2.0:0.0', 'v:3.0:0.0', {'label': 'E', 'B': 1}),
        ('v:3.0:0.0', 'v:3.0:1.0', {'label': 'E', 'B': 1}),
        ('v:3.0:1.0', 'v:2.0:1.0', {'label': 'E', 'B': 1}),
        ('v:2.0:1.0', 'v:2.0:0.0', {'label': 'E', 'B': 0}),

        ('Q:2.5:0.5', 'v:2.0:0.0'),
        ('Q:2.5:0.5', 'v:3.0:0.0'),
        ('Q:2.5:0.5', 'v:3.0:1.0'),
        ('Q:2.5:0.5', 'v:2.0:1.0'),
    ])

    return G


def test_two_graphs_to_cover_p8():
    graph = big_graph_specific()
    production = ProductionP8(graph)
    if view:
        plot_graph(graph, "TEST 7")

    # # Check initial conditions of the production
    assert graph.nodes['Q:0.5:0.5']['R'] == 0, "Node Q:0.5:0.5 should have R=0 before applying the production"
    assert graph.nodes['Q:1.5:1.5']['R'] == 0, "Node Q:0.5:0.5 should have R=0 before applying the production"
    assert graph.nodes['Q:2.5:0.5']['R'] == 0, "Node Q:2.5:0.5 should have R=0 before applying the production"

    assert graph.nodes['Q:1.25:0.75']['R'] == 1, "Node Q:1.25:0.75 should have R=1 before applying the production"
    assert graph.nodes['Q:1.25:0.25']['R'] == 1, "Node Q:1.25:0.25 should have R=1 before applying the production"
    assert graph.nodes['Q:1.75:0.75']['R'] == 1, "Node Q:1.75:0.75 should have R=1 before applying the production"
    assert graph.nodes['Q:1.75:0.25']['R'] == 1, "Node Q:1.75:0.25 should have R=1 before applying the production"

    assert graph.nodes['v:1.0:0.5']['h'] == 1, "Node v:1.0:0.5 should be a.py hanging node (h=1)"
    assert graph.nodes['v:1.5:1.0']['h'] == 1, "Node v:1.5:1.0 should be a.py hanging node (h=1)"
    assert graph.nodes['v:2.0:0.5']['h'] == 1, "Node v:1.5:1.0 should be a.py hanging node (h=1)"

    # Verify if the production correctly identifies hyper edges
    result = production.extract_left_side_to_specific_place("Q:1.25:0.75")
    assert result is not None, "No suitable nodes found for applying the production"

    # Apply the production
    production.apply_to_specific_place("Q:1.25:0.75")
    if view:
        plot_graph(graph, "TEST 7 - AFTER PRODUCTION")

    # Check conditions after the production
    assert graph.nodes['Q:0.5:0.5']['R'] == 1, "Node Q:0.5:0.5 should have R=0 before applying the production"
    assert graph.nodes['Q:1.5:1.5']['R'] == 1, "Node Q:0.5:0.5 should have R=0 before applying the production"
    assert graph.nodes['Q:2.5:0.5']['R'] == 0, "Node Q:2.5:0.5 should have R=0 before applying the production"

    assert graph.nodes['Q:1.25:0.75']['R'] == 1, "Node Q:1.25:0.75 should have R=1 before applying the production"
    assert graph.nodes['Q:1.25:0.25']['R'] == 1, "Node Q:1.25:0.25 should have R=1 before applying the production"
    assert graph.nodes['Q:1.75:0.75']['R'] == 1, "Node Q:1.75:0.75 should have R=1 before applying the production"
    assert graph.nodes['Q:1.75:0.25']['R'] == 1, "Node Q:1.75:0.25 should have R=1 before applying the production"

    assert graph.nodes['v:1.0:0.5']['h'] == 1, "Node v:1.0:0.5 should be a.py hanging node (h=1)"
    assert graph.nodes['v:1.5:1.0']['h'] == 1, "Node v:1.5:1.0 should be a.py hanging node (h=1)"
    assert graph.nodes['v:2.0:0.5']['h'] == 1, "Node v:1.5:1.0 should be a.py hanging node (h=1)"
