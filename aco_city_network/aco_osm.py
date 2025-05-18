import numpy as np

ALPHA = 1.0
BETA = 3.0
EVAPORATION = 0.5
Q = 100

def build_path(G, pheromone, start, end):
    path = [start]
    current = start
    while current != end:
        neighbors = list(G.neighbors(current))
        if not neighbors:
            return None
        probs = []
        for n in neighbors:
            edge = tuple(sorted((current, n)))
            pheromone[edge] = pheromone.get(edge, 1.0)
            weight = G[current][n].get('length', 1.0)
            tau = pheromone[edge] ** ALPHA
            eta = (1.0 / weight) ** BETA
            probs.append(tau * eta)
        probs = np.array(probs)
        probs /= probs.sum()
        next_node = np.random.choice(neighbors, p=probs)
        path.append(next_node)
        current = next_node
        if len(path) > len(G.nodes):
            return None
    return path

def path_cost(G, path):
    return sum(G[path[i]][path[i+1]].get('length', 1.0) for i in range(len(path)-1))

def ant_colony_optimization(G, start, end, num_ants=20, num_iter=50):
    pheromone = {}
    best_path, best_cost = None, float('inf')
    for _ in range(num_iter):
        all_paths = []
        for _ in range(num_ants):
            path = build_path(G, pheromone, start, end)
            if path:
                cost = path_cost(G, path)
                all_paths.append((path, cost))
                if cost < best_cost:
                    best_path, best_cost = path, cost
        for edge in pheromone:
            pheromone[edge] *= (1 - EVAPORATION)
        for path, cost in all_paths:
            for i in range(len(path) - 1):
                edge = tuple(sorted((path[i], path[i+1])))
                pheromone[edge] = pheromone.get(edge, 0) + Q / cost
    return best_path, best_cost
