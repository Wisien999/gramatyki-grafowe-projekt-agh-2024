import networkx as nx

from productions.p1.production1 import ProductionP1
from productions.utils import prepare_big_graph, prepare_basic_square_graph


def test_basic_4_nodes_graph():
    """ Verifies if structure is valid after applying production 1 to 4 nodes graph"""
    g = prepare_basic_square_graph()

    prod1 = ProductionP1(g)
    prod1.apply()

    expected_graph = {'Q:0.25:0.25': {'v:0.0:0.0': {},
                                     'v:0.0:0.5': {},
                                     'v:0.5:0.0': {},
                                     'v:0.5:0.5': {}},
                     'Q:0.25:0.75': {'v:0.0:0.5': {},
                                     'v:0.0:1.0': {},
                                     'v:0.5:0.5': {},
                                     'v:0.5:1.0': {}},
                     'Q:0.75:0.25': {'v:0.5:0.0': {},
                                     'v:0.5:0.5': {},
                                     'v:1.0:0.0': {},
                                     'v:1.0:0.5': {}},
                     'Q:0.75:0.75': {'v:0.5:0.5': {},
                                     'v:0.5:1.0': {},
                                     'v:1.0:0.5': {},
                                     'v:1.0:1.0': {}},
                     'v:0.0:0.0': {'Q:0.25:0.25': {},
                                   'v:0.0:0.5': {'B': 1, 'label': 'E'},
                                   'v:0.5:0.0': {'B': 1, 'label': 'E'}},
                     'v:0.0:0.5': {'Q:0.25:0.25': {},
                                   'Q:0.25:0.75': {},
                                   'v:0.0:0.0': {'B': 1, 'label': 'E'},
                                   'v:0.0:1.0': {'B': 1, 'label': 'E'},
                                   'v:0.5:0.5': {'B': 0, 'label': 'E'}},
                     'v:0.0:1.0': {'Q:0.25:0.75': {},
                                   'v:0.0:0.5': {'B': 1, 'label': 'E'},
                                   'v:0.5:1.0': {'B': 1, 'label': 'E'}},
                     'v:0.5:0.0': {'Q:0.25:0.25': {},
                                   'Q:0.75:0.25': {},
                                   'v:0.0:0.0': {'B': 1, 'label': 'E'},
                                   'v:0.5:0.5': {'B': 0, 'label': 'E'},
                                   'v:1.0:0.0': {'B': 1, 'label': 'E'}},
                     'v:0.5:0.5': {'Q:0.25:0.25': {},
                                   'Q:0.25:0.75': {},
                                   'Q:0.75:0.25': {},
                                   'Q:0.75:0.75': {},
                                   'v:0.0:0.5': {'B': 0, 'label': 'E'},
                                   'v:0.5:0.0': {'B': 0, 'label': 'E'},
                                   'v:0.5:1.0': {'B': 0, 'label': 'E'},
                                   'v:1.0:0.5': {'B': 0, 'label': 'E'}},
                     'v:0.5:1.0': {'Q:0.25:0.75': {},
                                   'Q:0.75:0.75': {},
                                   'v:0.0:1.0': {'B': 1, 'label': 'E'},
                                   'v:0.5:0.5': {'B': 0, 'label': 'E'},
                                   'v:1.0:1.0': {'B': 1, 'label': 'E'}},
                     'v:1.0:0.0': {'Q:0.75:0.25': {},
                                   'v:0.5:0.0': {'B': 1, 'label': 'E'},
                                   'v:1.0:0.5': {'B': 1, 'label': 'E'}},
                     'v:1.0:0.5': {'Q:0.75:0.25': {},
                                   'Q:0.75:0.75': {},
                                   'v:0.5:0.5': {'B': 0, 'label': 'E'},
                                   'v:1.0:0.0': {'B': 1, 'label': 'E'},
                                   'v:1.0:1.0': {'B': 1, 'label': 'E'}},
                     'v:1.0:1.0': {'Q:0.75:0.75': {},
                                   'v:0.5:1.0': {'B': 1, 'label': 'E'},
                                   'v:1.0:0.5': {'B': 1, 'label': 'E'}}}
    assert expected_graph == nx.to_dict_of_dicts(g)


def test_8_nodes_graph_with_2_applies():
    """ verifies if structure is the same after applying 2 production 1's on 8 nodes graph"""
    g = prepare_big_graph()

    prod1 = ProductionP1(g)
    prod1.apply()
    prod1.apply()

    expected_graph = {'Q:1.25:1.25': {'v:0.0:0.0': {},
                 'v:0.0:2.5': {},
                 'v:2.5:0.0': {},
                 'v:2.5:2.5': {}},
 'Q:1.25:3.75': {'v:0.0:2.5': {},
                 'v:0.0:5.0': {},
                 'v:2.5:2.5': {},
                 'v:2.5:5.0': {}},
 'Q:2.5:7.5': {'v:0.0:10.0': {},
               'v:0.0:5.0': {},
               'v:5.0:10.0': {},
               'v:5.0:5.0': {}},
 'Q:3.75:1.25': {'v:2.5:0.0': {},
                 'v:2.5:2.5': {},
                 'v:5.0:0.0': {},
                 'v:5.0:2.5': {}},
 'Q:3.75:3.75': {'v:2.5:2.5': {},
                 'v:2.5:5.0': {},
                 'v:5.0:2.5': {},
                 'v:5.0:5.0': {}},
 'Q:6.25:6.25': {'v:5.0:5.0': {},
                 'v:5.0:7.5': {},
                 'v:7.5:5.0': {},
                 'v:7.5:7.5': {}},
 'Q:6.25:8.75': {'v:5.0:10.0': {},
                 'v:5.0:7.5': {},
                 'v:7.5:10.0': {},
                 'v:7.5:7.5': {}},
 'Q:7.5:2.5': {'v:10.0:0.0': {},
               'v:10.0:5.0': {},
               'v:5.0:0.0': {},
               'v:5.0:5.0': {}},
 'Q:8.75:6.25': {'v:10.0:5.0': {},
                 'v:10.0:7.5': {},
                 'v:7.5:5.0': {},
                 'v:7.5:7.5': {}},
 'Q:8.75:8.75': {'v:10.0:10.0': {},
                 'v:10.0:7.5': {},
                 'v:7.5:10.0': {},
                 'v:7.5:7.5': {}},
 'v:0.0:0.0': {'Q:1.25:1.25': {},
               'v:0.0:2.5': {'B': 1, 'label': 'E'},
               'v:2.5:0.0': {'B': 1, 'label': 'E'}},
 'v:0.0:10.0': {'Q:2.5:7.5': {},
                'v:0.0:5.0': {'B': 1, 'label': 'E'},
                'v:5.0:10.0': {'B': 1, 'label': 'E'}},
 'v:0.0:2.5': {'Q:1.25:1.25': {},
               'Q:1.25:3.75': {},
               'v:0.0:0.0': {'B': 1, 'label': 'E'},
               'v:0.0:5.0': {'B': 1, 'label': 'E'},
               'v:2.5:2.5': {'B': 0, 'label': 'E'}},
 'v:0.0:5.0': {'Q:1.25:3.75': {},
               'Q:2.5:7.5': {},
               'v:0.0:10.0': {'B': 1, 'label': 'E'},
               'v:0.0:2.5': {'B': 1, 'label': 'E'},
               'v:2.5:5.0': {'B': 0, 'label': 'E'}},
 'v:10.0:0.0': {'Q:7.5:2.5': {},
                'v:10.0:5.0': {'B': 1, 'label': 'E'},
                'v:5.0:0.0': {'B': 1, 'label': 'E'}},
 'v:10.0:10.0': {'Q:8.75:8.75': {},
                 'v:10.0:7.5': {'B': 1, 'label': 'E'},
                 'v:7.5:10.0': {'B': 1, 'label': 'E'}},
 'v:10.0:5.0': {'Q:7.5:2.5': {},
                'Q:8.75:6.25': {},
                'v:10.0:0.0': {'B': 1, 'label': 'E'},
                'v:10.0:7.5': {'B': 1, 'label': 'E'},
                'v:7.5:5.0': {'B': 0, 'label': 'E'}},
 'v:10.0:7.5': {'Q:8.75:6.25': {},
                'Q:8.75:8.75': {},
                'v:10.0:10.0': {'B': 1, 'label': 'E'},
                'v:10.0:5.0': {'B': 1, 'label': 'E'},
                'v:7.5:7.5': {'B': 0, 'label': 'E'}},
 'v:2.5:0.0': {'Q:1.25:1.25': {},
               'Q:3.75:1.25': {},
               'v:0.0:0.0': {'B': 1, 'label': 'E'},
               'v:2.5:2.5': {'B': 0, 'label': 'E'},
               'v:5.0:0.0': {'B': 1, 'label': 'E'}},
 'v:2.5:2.5': {'Q:1.25:1.25': {},
               'Q:1.25:3.75': {},
               'Q:3.75:1.25': {},
               'Q:3.75:3.75': {},
               'v:0.0:2.5': {'B': 0, 'label': 'E'},
               'v:2.5:0.0': {'B': 0, 'label': 'E'},
               'v:2.5:5.0': {'B': 0, 'label': 'E'},
               'v:5.0:2.5': {'B': 0, 'label': 'E'}},
 'v:2.5:5.0': {'Q:1.25:3.75': {},
               'Q:3.75:3.75': {},
               'v:0.0:5.0': {'B': 0, 'label': 'E'},
               'v:2.5:2.5': {'B': 0, 'label': 'E'},
               'v:5.0:5.0': {'B': 0, 'label': 'E'}},
 'v:5.0:0.0': {'Q:3.75:1.25': {},
               'Q:7.5:2.5': {},
               'v:10.0:0.0': {'B': 1, 'label': 'E'},
               'v:2.5:0.0': {'B': 1, 'label': 'E'},
               'v:5.0:2.5': {'B': 0, 'label': 'E'}},
 'v:5.0:10.0': {'Q:2.5:7.5': {},
                'Q:6.25:8.75': {},
                'v:0.0:10.0': {'B': 1, 'label': 'E'},
                'v:5.0:7.5': {'B': 0, 'label': 'E'},
                'v:7.5:10.0': {'B': 1, 'label': 'E'}},
 'v:5.0:2.5': {'Q:3.75:1.25': {},
               'Q:3.75:3.75': {},
               'v:2.5:2.5': {'B': 0, 'label': 'E'},
               'v:5.0:0.0': {'B': 0, 'label': 'E'},
               'v:5.0:5.0': {'B': 0, 'label': 'E'}},
 'v:5.0:5.0': {'Q:2.5:7.5': {},
               'Q:3.75:3.75': {},
               'Q:6.25:6.25': {},
               'Q:7.5:2.5': {},
               'v:2.5:5.0': {'B': 0, 'label': 'E'},
               'v:5.0:2.5': {'B': 0, 'label': 'E'},
               'v:5.0:7.5': {'B': 0, 'label': 'E'},
               'v:7.5:5.0': {'B': 0, 'label': 'E'}},
 'v:5.0:7.5': {'Q:6.25:6.25': {},
               'Q:6.25:8.75': {},
               'v:5.0:10.0': {'B': 0, 'label': 'E'},
               'v:5.0:5.0': {'B': 0, 'label': 'E'},
               'v:7.5:7.5': {'B': 0, 'label': 'E'}},
 'v:7.5:10.0': {'Q:6.25:8.75': {},
                'Q:8.75:8.75': {},
                'v:10.0:10.0': {'B': 1, 'label': 'E'},
                'v:5.0:10.0': {'B': 1, 'label': 'E'},
                'v:7.5:7.5': {'B': 0, 'label': 'E'}},
 'v:7.5:5.0': {'Q:6.25:6.25': {},
               'Q:8.75:6.25': {},
               'v:10.0:5.0': {'B': 0, 'label': 'E'},
               'v:5.0:5.0': {'B': 0, 'label': 'E'},
               'v:7.5:7.5': {'B': 0, 'label': 'E'}},
 'v:7.5:7.5': {'Q:6.25:6.25': {},
               'Q:6.25:8.75': {},
               'Q:8.75:6.25': {},
               'Q:8.75:8.75': {},
               'v:10.0:7.5': {'B': 0, 'label': 'E'},
               'v:5.0:7.5': {'B': 0, 'label': 'E'},
               'v:7.5:10.0': {'B': 0, 'label': 'E'},
               'v:7.5:5.0': {'B': 0, 'label': 'E'}}}
    assert expected_graph == nx.to_dict_of_dicts(g)