import networkx as nx
#import ged4py
from ged4py.algorithm import graph_edit_dist

g = nx.Graph()
g.add_edge("A", "B")
g.add_node("C", weight=1)
g2 = g.copy()
g.add_edge("A", "C")


print(graph_edit_dist.compare(g, g2))
