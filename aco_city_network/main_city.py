import matplotlib.pyplot as plt
import osmnx as ox
from city_network import load_city_graph, get_nearest_nodes
from aco_osm import ant_colony_optimization

# Load graph and compute route
G = load_city_graph()
source_coords = (13.032230, 80.211797)
target_coords = (13.035937, 80.204351)
source_node, target_node = get_nearest_nodes(G, source_coords, target_coords)

best_path, best_cost = ant_colony_optimization(G, source_node, target_node)

print(f"Best path length: {best_cost}")
print(f"First few nodes: {best_path[:5]}")

# Plot result
fig, ax = ox.plot_graph_route(G, best_path, route_linewidth=4, node_size=0, bgcolor='white', figsize=(25, 25))
