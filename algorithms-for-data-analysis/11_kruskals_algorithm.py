import random

num_nodes = 4
num_edges = 10
max_edge_weight = 10

nodes = list(range(1, num_nodes + 1))
edges = []

while len(edges) < num_edges:
    u = random.choice(nodes)
    v = random.choice(nodes)
    
    if u != v:
        e = random.randint(1, max_edge_weight)
        edges.append([u, v, e])
print(f"Initial edges: {edges}")

sorted_edges = sorted(edges, key=lambda x: x[2])

nodes_in_tree = set([])
tree_edges = []
cost = 0

for edge in sorted_edges:
    if edge[0] not in nodes_in_tree or edge[1] not in nodes_in_tree:
        nodes_in_tree.add(edge[0])
        nodes_in_tree.add(edge[1])
        tree_edges.append(edge)
                                                       
print(f"Final edges: {tree_edges}")
print(f"Cost: {cost}")
