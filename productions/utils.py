import networkx as nx


def prepare_basic_square_graph() -> nx.Graph:
    """Prepares the basic 4-nodes and one Q-node graph"""
    G = nx.Graph()
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0})
    ])
    G.add_edges_from([
        ('v:0.0:0.0', 'v:1.0:0.0', {'label': 'E', 'B': 1}),
        ('v:1.0:0.0', 'v:1.0:1.0', {'label': 'E', 'B': 1}),
        ('v:1.0:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),
        ('v:0.0:1.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),
    ])
    add_hyperedge_to_graph(G, ['v:0.0:0.0', 'v:1.0:0.0', 'v:1.0:1.0', 'v:0.0:1.0'], hyperedge_label='Q', breakable=True)

    return G


def prepare_basic_square_with_hanging_node_graph() -> nx.Graph:
    """Prepares the basic 4-nodes and one Q-node + hanging node graph"""
    G = nx.Graph()
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),
        ('v:1.0:0.5', {'label': 'v', 'x': 1.0, 'y': 0.5, 'h': 1})
    ])
    G.add_edges_from([
        ('v:0.0:0.0', 'v:1.0:0.0', {'label': 'E', 'B': 1}),
        ('v:1.0:0.0', 'v:1.0:0.5', {'label': 'E', 'B': 1}),
        ('v:1.0:0.5', 'v:1.0:1.0', {'label': 'E', 'B': 1}),
        ('v:1.0:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),
        ('v:0.0:1.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),
    ])
    add_hyperedge_to_graph(G, ['v:0.0:0.0', 'v:1.0:0.0', 'v:1.0:1.0', 'v:0.0:1.0'], hyperedge_label='Q', breakable=True)

    return G

def prepare_valid_test_graph_with_hanging_node_p3() -> nx.Graph:
    """Prepares the basic 4-nodes and one Q-node graph"""
    G = nx.Graph()
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),
        ('v:1.0:0.5', {'label': 'v', 'x': 1.0, 'y': 0.5, 'h': 1}),
        ('v:0.5:0.0', {'label': 'v', 'x': 0.5, 'y': 0.0, 'h': 1})

    ])
    G.add_edges_from([
        ('v:0.0:0.0', 'v:0.5:0.0', {'label': 'E', 'B': 1}),
        ('v:0.5:0.0', 'v:1.0:0.0', {'label': 'E', 'B': 1}),
        ('v:1.0:0.0', 'v:1.0:0.5', {'label': 'E', 'B': 1}),
        ('v:1.0:0.5', 'v:1.0:1.0', {'label': 'E', 'B': 1}),
        ('v:1.0:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),
        ('v:0.0:1.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),
    ])
    add_hyperedge_to_graph(G, ['v:0.0:0.0', 'v:1.0:0.0', 'v:1.0:1.0', 'v:0.0:1.0'], hyperedge_label='Q', breakable=True)

    return G

def prepare_valid_test_graph_with_hanging_node_p4() -> nx.Graph:
    """Prepares the basic 4-nodes and one Q-node graph"""
    G = nx.Graph()
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1.0, 'y': 0.0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0.0, 'y': 1.0, 'h': 0}),
        ('v:0.0:0.5', {'label': 'v', 'x': 0.0, 'y': 0.5, 'h': 1}),
        ('v:1.0:0.5', {'label': 'v', 'x': 1.0, 'y': 0.5, 'h': 1})

    ])
    G.add_edges_from([
        ('v:0.0:0.0', 'v:0.0:0.5', {'label': 'E', 'B': 1}),
        ('v:0.0:0.5', 'v:0.0:1.0', {'label': 'E', 'B': 1}),
        ('v:1.0:0.0', 'v:1.0:0.5', {'label': 'E', 'B': 1}),
        ('v:1.0:0.5', 'v:1.0:1.0', {'label': 'E', 'B': 1}),
        ('v:1.0:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),
        ('v:0.0:1.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),
        ('v:0.0:0.0', 'v:1.0:0.0', {'label': 'E', 'B': 1}),
    ])
    add_hyperedge_to_graph(G, ['v:0.0:0.0', 'v:1.0:0.0', 'v:1.0:1.0', 'v:0.0:1.0'], hyperedge_label='Q', breakable=True)

    return G

def prepare_basic_square_without_hyperedge_graph() -> nx.Graph:
    """Prepares the basic 4-nodes graph"""
    G = nx.Graph()
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0, 'y': 0, 'h': 0}),
        ('v:1.0:0.0', {'label': 'v', 'x': 1, 'y': 0, 'h': 0}),
        ('v:1.0:1.0', {'label': 'v', 'x': 1, 'y': 1, 'h': 0}),
        ('v:0.0:1.0', {'label': 'v', 'x': 0, 'y': 1, 'h': 0})
    ])
    G.add_edges_from([
        ('v:0.0:0.0', 'v:1.0:0.0', {'label': 'E', 'B': 1}),
        ('v:1.0:0.0', 'v:1.0:1.0', {'label': 'E', 'B': 1}),
        ('v:1.0:1.0', 'v:0.0:1.0', {'label': 'E', 'B': 1}),
        ('v:0.0:1.0', 'v:0.0:0.0', {'label': 'E', 'B': 1}),
    ])

    return G

def prepare_big_graph() -> nx.Graph:
    G = nx.Graph()
    G.add_nodes_from([
        ('v:0.0:0.0', {'label': 'v', 'x': 0.0, 'y': 0.0, 'h': 0}),
        ('v:5.0:0.0', {'label': 'v', 'x': 5.0, 'y': 0.0, 'h': 0}),
        ('v:10.0:0.0', {'label': 'v', 'x': 10.0, 'y': 0.0, 'h': 0}),
        ('v:10.0:5.0', {'label': 'v', 'x': 10.0, 'y': 5.0, 'h': 0}),
        ('v:10.0:10.0', {'label': 'v', 'x': 10.0, 'y': 10.0, 'h': 0}),
        ('v:5.0:10.0', {'label': 'v', 'x': 5.0, 'y': 10.0, 'h': 0}),
        ('v:0.0:10.0', {'label': 'v', 'x': 0.0, 'y': 10.0, 'h': 0}),
        ('v:0.0:5.0', {'label': 'v', 'x': 0.0, 'y': 5.0, 'h': 0}),
        ('v:5.0:5.0', {'label': 'v', 'x': 5.0, 'y': 5.0, 'h': 0}),

        ('v:2.5:5.0', {'label': 'v', 'x': 2.5, 'y': 5.0, 'h': 1}),
        ('v:0.0:2.5', {'label': 'v', 'x': 0.0, 'y': 2.5, 'h': 0}),
        ('v:2.5:0.0', {'label': 'v', 'x': 2.5, 'y': 0.0, 'h': 0}),
        ('v:5.0:2.5', {'label': 'v', 'x': 5.0, 'y': 2.5, 'h': 1}),
        ('v:2.5:2.5', {'label': 'v', 'x': 2.5, 'y': 2.5, 'h': 0}),

        ('Q:2.5:7.5', {'label': 'Q', 'R': 1}),
        ('Q:7.5:7.5', {'label': 'Q', 'R': 1}),
        ('Q:7.5:2.5', {'label': 'Q', 'R': 0}),

        ('Q:1.25:1.25', {'label': 'Q', 'R': 0}),
        ('Q:1.25:3.75', {'label': 'Q', 'R': 0}),
        ('Q:3.75:1.25', {'label': 'Q', 'R': 0}),
        ('Q:3.75:3.75', {'label': 'Q', 'R': 0})
    ])
    G.add_edges_from([
        ('v:0.0:0.0', 'v:2.5:0.0', {'label': 'E', 'B': 1}),
        ('v:2.5:0.0', 'v:5.0:0.0', {'label': 'E', 'B': 1}),
        ('v:5.0:0.0', 'v:10.0:0.0', {'label': 'E', 'B': 1}),
        ('v:10.0:0.0', 'v:10.0:5.0', {'label': 'E', 'B': 1}),
        ('v:10.0:5.0', 'v:10.0:10.0', {'label': 'E', 'B': 1}),
        ('v:10.0:10.0', 'v:5.0:10.0', {'label': 'E', 'B': 1}),
        ('v:5.0:10.0', 'v:0.0:10.0', {'label': 'E', 'B': 1}),
        ('v:0.0:10.0', 'v:0.0:5.0', {'label': 'E', 'B': 1}),
        ('v:0.0:5.0', 'v:0.0:2.5', {'label': 'E', 'B': 1}),
        ('v:0.0:2.5', 'v:0.0:0.0', {'label': 'E', 'B': 1}),

        ('v:5.0:5.0', 'v:10.0:5.0', {'label': 'E', 'B': 0}),
        ('v:5.0:5.0', 'v:5.0:10.0', {'label': 'E', 'B': 0}),

        ('v:0.0:5.0', 'v:2.5:5.0', {'label': 'E', 'B': 0}),
        ('v:2.5:5.0', 'v:5.0:5.0', {'label': 'E', 'B': 0}),
        ('v:5.0:5.0', 'v:5.0:2.5', {'label': 'E', 'B': 0}),
        ('v:5.0:2.5', 'v:5.0:0.0', {'label': 'E', 'B': 0}),

        ('v:0.0:2.5', 'v:2.5:2.5', {'label': 'E', 'B': 0}),
        ('v:2.5:5.0', 'v:2.5:2.5', {'label': 'E', 'B': 0}),
        ('v:5.0:2.5', 'v:2.5:2.5', {'label': 'E', 'B': 0}),
        ('v:2.5:0.0', 'v:2.5:2.5', {'label': 'E', 'B': 0}),

        ('Q:2.5:7.5', 'v:5.0:10.0'), ('Q:2.5:7.5', 'v:0.0:10.0'), ('Q:2.5:7.5', 'v:0.0:5.0'), ('Q:2.5:7.5', 'v:5.0:5.0'),
        ('Q:7.5:7.5', 'v:5.0:5.0'), ('Q:7.5:7.5', 'v:10.0:5.0'), ('Q:7.5:7.5', 'v:10.0:10.0'), ('Q:7.5:7.5', 'v:5.0:10.0'),
        ('Q:7.5:2.5', 'v:5.0:5.0'), ('Q:7.5:2.5', 'v:5.0:0.0'), ('Q:7.5:2.5', 'v:10.0:0.0'), ('Q:7.5:2.5', 'v:10.0:5.0'),

        ('Q:1.25:1.25', 'v:2.5:2.5'), ('Q:1.25:1.25', 'v:0.0:0.0'), ('Q:1.25:1.25', 'v:0.0:2.5'), ('Q:1.25:1.25', 'v:2.5:0.0'), 
        ('Q:1.25:3.75', 'v:0.0:5.0'), ('Q:1.25:3.75', 'v:2.5:5.0'), ('Q:1.25:3.75', 'v:2.5:2.5'), ('Q:1.25:3.75', 'v:0.0:2.5'), 
        ('Q:3.75:1.25', 'v:2.5:2.5'), ('Q:3.75:1.25', 'v:2.5:0.0'), ('Q:3.75:1.25', 'v:5.0:0.0'), ('Q:3.75:1.25', 'v:5.0:2.5'), 
        ('Q:3.75:3.75', 'v:2.5:2.5'), ('Q:3.75:3.75', 'v:2.5:5.0'), ('Q:3.75:3.75', 'v:5.0:5.0'), ('Q:3.75:3.75', 'v:5.0:2.5'), 
    ])

    return G

def add_hyperedge_to_graph(G: nx.Graph, nodes: list, hyperedge_label='Q',  breakable=True):
    """Add a hyperedge to the graph G."""
    G.add_node(hyperedge_label, label=hyperedge_label, R=1 if breakable else 0)
    G.add_edges_from([(node, hyperedge_label) for node in nodes])
