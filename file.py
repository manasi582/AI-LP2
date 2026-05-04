from collections import deque

# ----------- GRAPH INPUT -----------

def create_graph():
    while True:
        choice = input("Enter graph manually? (y/n): ").strip().lower()
        if choice in ['y', 'n']:
            break
        print("Please enter only 'y' or 'n'")

    if choice == 'y':
        n = int(input("Enter number of vertices: "))
        e = int(input("Enter number of edges: "))

        # Use 1-based indexing (more intuitive)
        graph = {i: [] for i in range(1, n + 1)}

        print("Enter edges (u v):")
        for _ in range(e):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)   # undirected

    else:
        print("Using default graph...")
        graph = {
            1: [2, 3, 4],
            2: [1, 5],
            3: [1, 5],
            4: [1, 5],
            5: [2, 3, 4]
        }

    return graph


# ----------- DFS (RECURSIVE) -----------

def dfs(graph, node, visited):
    visited.add(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# ----------- BFS -----------

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# ----------- MAIN -----------

print("=== GRAPH TRAVERSAL PROGRAM ===")

graph = create_graph()

print("\nAdjacency List:")
for node in graph:
    print(f"{node} -> {' '.join(map(str, graph[node]))}")

# Take starting nodes
start_dfs = int(input("\nEnter starting node for DFS: "))
start_bfs = int(input("Enter starting node for BFS: "))

# DFS
print("\nDFS Traversal:", end=" ")
dfs(graph, start_dfs, set())

# BFS
print("\nBFS Traversal:", end=" ")
bfs(graph, start_bfs)