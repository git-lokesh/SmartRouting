import networkx as nx
import osmnx as ox

def load_city_graph(place="Chennai, Tamil Nadu, India"):
    G = ox.graph_from_place(place, network_type='drive')
    G = G.to_undirected()
    largest_cc = max(nx.connected_components(G), key=len)
    return G.subgraph(largest_cc).copy()

def get_nearest_nodes(G, source_coords, target_coords):
    source_node = ox.distance.nearest_nodes(G, source_coords[1], source_coords[0])
    target_node = ox.distance.nearest_nodes(G, target_coords[1], target_coords[0])
    return source_node, target_node
