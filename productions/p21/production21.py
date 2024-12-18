from itertools import combinations

from ..production import Production


class ProductionP21(Production):
    """
    Production P21:
    Marks the hexagon elements as breakable. 
    """

    @property
    def check(self):
        """Checks if the production can be applied to the selected hexagon."""
        for node, data in self.graph.nodes(data=True):
            if data.get("label") == "S" and data.get("R") == 0:
                print("check passed")
                neighbors = list(self.graph.neighbors(node))
                return self._extract_subgraph(node, neighbors)
        print("didnt pass check")
        return None

    def apply(self):
        """Apply P21 to mark the hexagon elements as breakable."""

        result = self.check
        if result:
            r_node, neighbors = result
            self.graph.nodes[r_node]['R'] = 1 

"""
from fake_graphs import *
from plot_graph import plot_graph
from productions.p21.production21 import ProductionP21

if __name__ == '__main__':
    G = nx.Graph()
    
    G.add_node("S:5.0:5.0", label="S", R=0)
    G.add_nodes_from(
        [
            ("v:0.0:0.0", {"label": "v", "x": 0.0, "y": 0.0, "h": 0}),
            ("v:10.0:0.0", {"label": "v", "x": 10.0, "y": 0.0, "h": 0}),
            ("v:5.0:15.0", {"label": "v", "x": 5.0, "y": 15.0, "h": 0}),
            ("v:0.0:5.0", {"label": "v", "x": 0.0, "y": 5.0, "h": 0}),
            ("v:15.0:5.0", {"label": "v", "x": 15.0, "y": 5.0, "h": 0}),
            ("v:15.0:15.0", {"label": "v", "x": 15.0, "y": 15.0, "h": 0}), # added
        ]
    )
    G.add_edges_from(
        [
            ("S:5.0:5.0", "v:0.0:0.0"),
            ("S:5.0:5.0", "v:15.0:5.0"),
            ("S:5.0:5.0", "v:10.0:0.0"),
            ("S:5.0:5.0", "v:5.0:15.0"),
            ("S:5.0:5.0", "v:0.0:5.0"),
            ("S:5.0:5.0", "v:15.0:15.0"), # added
        ]
    )

    plot_graph(G)
    prod21 = ProductionP21(G)
    prod21.apply()
    plot_graph(G)
"""