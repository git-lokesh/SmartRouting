import random

ALPHA = 1.0
BETA = 2.0
EVAPORATION = 0.5
Q = 100

def build_path(G, pheromone, start, end):
    path = [start]
    cost = 0
    visited = set([start])

    while path[-1] != end:
        current = path[-1]
        neighbors = [n for n in G.neighbors(current) if n not in visited]
        if not neighbors:
            return path, float('inf')
        probs = []
        for n in neighbors:
            edge = tuple(sorted((current, n)))
            weight = G[current][n]['weight']
            tau = pheromone[edge] ** ALPHA
            eta = (1.0 / weight) ** BETA
            probs.append(tau * eta)
        total = sum(probs)
        probs = [p / total for p in probs]
        next_node = random.choices(neighbors, weights=probs)[0]
        path.append(next_node)
        cost += G[current][next_node]['weight']
        visited.add(next_node)

    return path, cost

def ant_colony_optimization(G, start, end, num_ants=10, num_iter=100):
    pheromone = {tuple(sorted(edge)): 1.0 for edge in G.edges()}
    best_path, best_cost = None, float('inf')

    for _ in range(num_iter):
        all_paths = []
        for _ in range(num_ants):
            path, cost = build_path(G, pheromone, start, end)
            all_paths.append((path, cost))
            if cost < best_cost:
                best_path, best_cost = path, cost
        for edge in pheromone:
            pheromone[edge] *= (1 - EVAPORATION)
        for path, cost in all_paths:
            for i in range(len(path) - 1):
                edge = tuple(sorted((path[i], path[i+1])))
                pheromone[edge] += Q / cost

    return best_path, best_cost
