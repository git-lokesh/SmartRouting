import matplotlib.pyplot as plt
import networkx as nx
from water_network import create_water_network
from aco_water import ant_colony_optimization

G = create_water_network()
start, end = 'Reservoir', 'C'
best_path, best_cost = ant_colony_optimization(G, start, end)

print(f"Best path from {start} to {end}: {best_path}")
print(f"Total pipe distance: {best_cost}")

# Visualization
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
path_edges = [(best_path[i], best_path[i+1]) for i in range(len(best_path)-1)]
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=3)
plt.title("Optimized Water Distribution Path")
plt.show()
