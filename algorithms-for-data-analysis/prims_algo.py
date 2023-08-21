import random
import pprint

def generate_random_graph(num_nodes):
    graph = [[0] * num_nodes for _ in range(num_nodes)]
    
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            weight = random.randint(1, 10)
            graph[i][j] = weight
            graph[j][i] = weight
    
    return graph

graph = generate_random_graph(5)
pprint.pprint(graph)

prims_graph = [[0] * len(graph) for _ in range(len(graph))]

dict = {}
for i in range(len(graph)):
    for j in range(len(graph)):
        if graph[i][j] != 0:
            if graph[i][j] not in dict:
                dict[graph[i][j]] = [(i, j)]
            else:
                dict[graph[i][j]].append((i, j))

keys = list(dict.keys())
keys.sort()

prims_nodes = []
for key in keys:
    for edge in dict[key]:
        if edge[0] not in prims_nodes or edge[1] not in prims_nodes:
            prims_nodes.append(edge[0])
            prims_nodes.append(edge[1])
            prims_graph[edge[0]][edge[1]] = key
            prims_graph[edge[1]][edge[0]] = key

pprint.pprint(prims_graph)