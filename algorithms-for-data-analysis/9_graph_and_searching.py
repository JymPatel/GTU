import random
initial_node = 0
number_of_nodes = 5

graph = [[random.randint(0, 1) for i in range(number_of_nodes)] for j in range(number_of_nodes)]
graph = [[1, 1, 0, 1, 0], [0, 1, 1, 1, 1], [0, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 1, 1, 1, 0]]


def dfs(graph_arr):
    print("DFS:")
    no_nodes = len(graph_arr)
    dfs_graph = [[0 for i in range(no_nodes)] for j in range(no_nodes)]

    to_visit = [initial_node]
    to_visit2 = [initial_node]
    visited = []

    while to_visit:
        curr = to_visit.pop()
        parent = to_visit2.pop()

        if curr in visited:
            continue
        # print(curr, ":)")

        dfs_graph[parent][curr] = 1
        for i in range(no_nodes):
            if not graph_arr[curr][i] or i in visited or i == curr:
                continue
            to_visit.append(i)
            to_visit2.append(curr)
            # print(to_visit, visited, ":)")
            # print(to_visit2, ":)")
        visited.append(curr)
        print(f"{curr}: {to_visit}")

    dfs_graph[initial_node][initial_node] = 0
    
    return dfs_graph



def bfs(graph_arr):
    print("BFS:")
    no_nodes = len(graph_arr)
    bfs_graph = [[0 for i in range(no_nodes)] for j in range(no_nodes)]

    to_visit = [initial_node]
    to_visit2 = [initial_node]
    visited = []

    while to_visit:
        curr = to_visit.pop(0)
        parent = to_visit2.pop(0)

        if curr in visited:
            continue
        print(curr, end=" ")

        bfs_graph[parent][curr] = 1
        for i in range(no_nodes):
            if not graph_arr[curr][i] or i in visited or i == curr:
                continue
            to_visit.append(i)
            to_visit2.append(curr)
            # print(to_visit, visited, ":)")
            # print(to_visit2, ":)")
        visited.append(curr)

    bfs_graph[initial_node][initial_node] = 0
    print()
    return bfs_graph
print(graph)
print(f"DFS: {dfs(graph)}")
print(f"BFS: {bfs(graph)}")

