from itertools import combinations
import networkx as nx
from statistics import fmean
from typing import Any, Optional

from productions.production import Production


class ProductionP5(Production):
    """
    Produkcja P5:
    (R=1), 4 narożne węzły h=0 i 3 węzły h=1 na trzech krawędziach.
    Po zastosowaniu produkcji powstają 4 mniejsze elementy, a h=1 węzły stają się h=0.
    """

    def extract_left_side(self):
        for node, data in self.graph.nodes(data=True):
            if is_hyperedge_node(data) and can_be_splitted(data):
                neighbors = list(self.graph.neighbors(node))
                if len(neighbors) == 4 and all_are_not_hanging_node(self.graph, neighbors):
                    m_nodes = find_three_hanging_nodes(self.graph, neighbors)
                    if m_nodes is not None:
                        return self._extract_subgraph(node, neighbors + m_nodes), m_nodes
        return None

    def apply(self):
        result = self.extract_left_side()
        if result is None:
            raise ApplyException("The operation could not be applied: result from extract_left_side() is None.")
        
        (q, neighbors_and_m_nodes), m_nodes = result
        corners = neighbors_and_m_nodes[:4]

        self.subgraph.remove_node(q)
        self.graph.remove_node(q)

        midpoints = {}
        for m in m_nodes:
            corner_pair = find_corner_pair_for_middle(self.subgraph, m, corners)
            if corner_pair is not None:
                a, b = corner_pair
                midpoints[m] = (a, b)

        for (n1, n2) in combinations(corners, 2):
            if self.subgraph.has_edge(n1, n2):
                if not has_middle_node_on_edge(self.subgraph, n1, n2, m_nodes):
                    self._create_midpoint(midpoints, n1, n2)

        phantom_edge_data = {}
        for m in m_nodes:
            (a, b) = midpoints[m]
            edge_data_am = self.graph.get_edge_data(a, m) or self.graph.get_edge_data(m, a)
            edge_data_bm = self.graph.get_edge_data(b, m) or self.graph.get_edge_data(m, b)
            
            edge_data_ab = edge_data_am or edge_data_bm
            if edge_data_ab:
                phantom_edge_data[(a, b)] = edge_data_ab

        self._fill_graph(corners, midpoints, edge_data=phantom_edge_data)

        for m in m_nodes:
            self.subgraph.nodes[m]['h'] = 0

        self.graph.update(self.subgraph)


def is_hyperedge_node(data):
    return data.get('label') == 'Q'


def can_be_splitted(data):
    return data.get('R') == 1


def all_are_not_hanging_node(graph, neighbors):
    return all(graph.nodes[n].get('h') == 0 for n in neighbors)


def find_three_hanging_nodes(graph: nx.Graph, corners: list) -> Optional[list]:
    hanging_nodes = []
    for (c1, c2) in combinations(corners, 2):
        m = find_middlepoint_with_h1(graph, c1, c2)
        if m is not None:
            hanging_nodes.append(m)

    if len(hanging_nodes) == 3:
        return hanging_nodes
    return None


def find_middlepoint_with_h1(graph: nx.Graph, n1, n2):
    for n in graph.neighbors(n1):
        if n in graph.neighbors(n2) and not is_hyperedge_node(graph.nodes[n]) and graph.nodes[n].get('h') == 1:
            return n
    return None


def find_corner_pair_for_middle(graph: nx.Graph, m, corners):
    c = []
    for nbr in graph.neighbors(m):
        if nbr in corners:
            c.append(nbr)
    if len(c) == 2:
        return c[0], c[1]
    return None


def has_middle_node_on_edge(graph: nx.Graph, n1, n2, m_nodes):
    for m in m_nodes:
        if (graph.has_edge(n1, m) and graph.has_edge(n2, m)):
            return True
    return False

class ApplyException(Exception):
    """Custom exception for when apply() cannot be performed."""
    pass