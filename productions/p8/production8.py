import itertools
from itertools import combinations

from productions.production import Production


class ProductionP8(Production):
    """
    Production P8:
    If a "small" element is marked for breaking, mark the adjacent "large" element for breaking as well.

    Conditions:
    - (R1 == 0) and (R2 == 1) and (h5 = 1)

    After applying the production:
    - R1 is set to 1
    - R2 remains 1 (marked for breaking)
    - h5 remains a hanging node
    """

    def extract_left_side(self):
        q_nodes = [node for node, data in self.graph.nodes(data=True) if data.get('label') == 'Q']
        q_nodes_r_1 = [node for node in q_nodes if self.graph.nodes[node].get('R') == 1]
        q_nodes_r_0 = [node for node in q_nodes if self.graph.nodes[node].get('R') == 0]

        for q_node_r_0, q_node_r_1 in itertools.product(q_nodes_r_0, q_nodes_r_1):
            if ((self._has_exactly_one_neighbor(q_node_r_0, q_node_r_1) and
                 self._check_if_hanging_node_on_the_way(q_node_r_0, q_node_r_1)) and
                    self._has_exactly_four_vertex(q_node_r_1)):
                return self._extract_subgraph(q_node_r_0, list(self.graph.neighbors(q_node_r_0)))
        return None

    def apply(self):
        while True:
            result = self.extract_left_side()
            if result is None:
                return

            node, left_side = result
            self.subgraph.nodes[node]['R'] = 1
            self.graph.update(self.subgraph)

    def _has_exactly_one_neighbor(self, node1, node2):
        return len(set(list(self.graph.neighbors(node1))) & set(list(self.graph.neighbors(node2)))) == 1

    def _has_exactly_four_vertex(self, q_node):
        return len(list(self.graph.neighbors(q_node))) == 4

    def _check_if_hanging_node_on_the_way(self, q_node_r_0, q_node_r_1):
        q_node_r_0_neighbors = list(self.graph.neighbors(q_node_r_0))
        q_node_r_1_neighbors = list(self.graph.neighbors(q_node_r_1))

        for node in q_node_r_1_neighbors:
            if self.graph.nodes[node].get('h') == 1:
                hanging_node = node
                for node1, node2 in combinations(q_node_r_0_neighbors, 2):
                    if hanging_node in self.graph.neighbors(node1) and hanging_node in self.graph.neighbors(node2):
                        return True

        return False

    def extract_left_side_to_specific_place(self, q_node_r_1):
        q_nodes = [node for node, data in self.graph.nodes(data=True) if data.get('label') == 'Q']
        q_nodes_r_0 = [node for node in q_nodes if self.graph.nodes[node].get('R') == 0]

        for q_node_r_0 in q_nodes_r_0:
            if (self._has_exactly_one_neighbor(q_node_r_0, q_node_r_1) and
                    self._check_if_hanging_node_on_the_way(q_node_r_0, q_node_r_1) and
                    self._has_exactly_four_vertex(q_node_r_1)):
                return self._extract_subgraph(q_node_r_0, list(self.graph.neighbors(q_node_r_0)))
        return None

    def apply_to_specific_place(self, node_to_break):
        if not (node_to_break in self.graph.nodes and
                self.graph.nodes[node_to_break].get('label') == 'Q' and
                self.graph.nodes[node_to_break].get('R') == 1):
            return

        for i in range(len(list(self.graph.neighbors(node_to_break)))):
            result = self.extract_left_side_to_specific_place(node_to_break)
            if result is None:
                continue

            node, left_side = result
            self.subgraph.nodes[node]['R'] = 1
            self.graph.update(self.subgraph)


def is_hyper_edge_node(data):
    return data.get('label') == 'Q'


def can_be_split(data):
    return data.get('R') == 1
