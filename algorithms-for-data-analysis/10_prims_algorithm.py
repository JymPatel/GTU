import random

def generate_random_graph(num_nodes):
    graph = [[0] * num_nodes for _ in range(num_nodes)]
    
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            weight = random.randint(1, 10)
            graph[i][j] = weight
            graph[j][i] = weight
    
    return graph

graph = generate_random_graph(4)
print(f"Initial graph: \n{graph}")


connected_nodes = set([0])
disconnected_nodes = set(range(1, len(graph)))

prims_graph = [[float('inf')] * len(graph[0]) for _ in range(len(graph))]
for i in range(len(prims_graph)):
    prims_graph[i][i] = 0

while disconnected_nodes:
    min_edge = None
    min_edge_weight = float('inf')
    for node in connected_nodes:
        for i in range(len(graph[node])):
            if i in disconnected_nodes:
                if graph[node][i] < min_edge_weight:
                    min_edge = (node, i)
                    min_edge_weight = graph[node][i]
    prims_graph[min_edge[0]][min_edge[1]] = min_edge_weight
    prims_graph[min_edge[1]][min_edge[0]] = min_edge_weight
    connected_nodes.add(min_edge[1])
    disconnected_nodes.remove(min_edge[1])

print(f"Final graph: \n{prims_graph}")
