import networkx as nx

def create_water_network():
    G = nx.Graph()
    edges = [
        ('Reservoir', 'A', 40), ('Reservoir', 'B', 2),
        ('A', 'C', 5), ('A', 'D', 10),
        ('B', 'D', 3), ('C', 'E', 4),
        ('D', 'E', 4), ('D', 'F', 6),
        ('E', 'F', 7)
    ]
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)
    return G
