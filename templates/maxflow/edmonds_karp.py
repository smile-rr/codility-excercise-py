from collections import deque

def bfs(capacity, source, sink, parent):
    """Performs BFS to find an augmenting path in the residual graph."""
    n = len(capacity)
    visited = [False] * n
    queue = deque([source])
    visited[source] = True

    while queue:
        u = queue.popleft()
        for v in range(n):
            if not visited[v] and capacity[u][v] > 0:  # If there's residual capacity and not yet visited
                queue.append(v)
                visited[v] = True
                parent[v] = u  # Store path
                if v == sink:
                    return True  # Found path to sink
    return False

def edmonds_karp(n, source, sink, capacity):
    """Computes the maximum flow using the Edmonds-Karp algorithm."""
    parent = [-1] * n
    max_flow = 0

    while bfs(capacity, source, sink, parent):
        # Find the maximum flow through the path found by BFS
        path_flow = float('Inf')
        v = sink

        while v != source:
            u = parent[v]
            path_flow = min(path_flow, capacity[u][v])
            v = u

        # Update the capacities of the edges and reverse edges along the path
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = u

        max_flow += path_flow

    return max_flow

# Example usage
n = 6  # Number of nodes
source, sink = 0, 5

# Capacity matrix
capacity = [[0, 16, 13, 0, 0, 0],
            [0, 0, 10, 12, 0, 0],
            [0, 4, 0, 0, 14, 0],
            [0, 0, 9, 0, 0, 20],
            [0, 0, 0, 7, 0, 4],
            [0, 0, 0, 0, 0, 0]]

max_flow = edmonds_karp(n, source, sink, capacity)
print("The maximum flow is:", max_flow)