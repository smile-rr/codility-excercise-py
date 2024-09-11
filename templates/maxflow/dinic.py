from collections import deque

def add_edge(adj, capacity, u, v, cap):
    """Adds a directed edge u -> v with the given capacity."""
    adj[u].append(len(capacity))  # Add the edge index to the adjacency list of u
    capacity.append([v, cap])  # Capacity for forward edge (u -> v)
    
    adj[v].append(len(capacity))  # Add the reverse edge index to adjacency list of v
    capacity.append([u, 0])  # Capacity for reverse edge (v -> u)

def bfs(level, adj, capacity, source, sink):
    """Constructs a level graph using BFS."""
    for i in range(len(level)):
        level[i] = -1  # Reset levels
    
    queue = deque([source])
    level[source] = 0

    while queue:
        u = queue.popleft()
        for i in adj[u]:
            v, cap = capacity[i]
            if level[v] == -1 and cap > 0:  # If v is not yet visited and capacity > 0
                level[v] = level[u] + 1
                queue.append(v)
                if v == sink:
                    return True  # Early exit if sink is reached
    return level[sink] != -1

def dfs(ptr, adj, capacity, level, u, sink, flow):
    """Finds a blocking flow using DFS."""
    if u == sink:
        return flow
    total_flow = 0
    while ptr[u] < len(adj[u]):
        i = adj[u][ptr[u]]
        v, cap = capacity[i]
        if level[v] == level[u] + 1 and cap > 0:
            min_cap = min(flow, cap)
            pushed_flow = dfs(ptr, adj, capacity, level, v, sink, min_cap)
            if pushed_flow > 0:
                capacity[i][1] -= pushed_flow  # Reduce forward edge capacity
                capacity[i ^ 1][1] += pushed_flow  # Increase reverse edge capacity
                total_flow += pushed_flow
                flow -= pushed_flow
                if flow == 0:
                    break
        ptr[u] += 1
    return total_flow

def dinic_max_flow(n, source, sink, edges):
    """Computes the maximum flow using Dinic's Algorithm."""
    adj = [[] for _ in range(n)]
    capacity = []
    for u, v, cap in edges:
        add_edge(adj, capacity, u, v, cap)

    max_flow = 0
    level = [-1] * n
    while bfs(level, adj, capacity, source, sink):
        ptr = [0] * n
        while True:
            pushed = dfs(ptr, adj, capacity, level, source, sink, float('inf'))
            if pushed == 0:
                break
            max_flow += pushed

    return max_flow

# Example usage
n = 6  # Number of nodes
source, sink = 0, 5
edges = [
    (0, 1, 10),
    (0, 2, 10),
    (1, 3, 4),
    (1, 4, 8),
    (1, 2, 2),
    (2, 4, 9),
    (3, 5, 10),
    (4, 3, 6),
    (4, 5, 10)
]

max_flow = dinic_max_flow(n, source, sink, edges)
print("The maximum flow is:", max_flow)