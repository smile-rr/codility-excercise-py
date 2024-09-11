from collections import deque

def add_edge(adj, capacity, u, v, cap):
    """Adds a directed edge u -> v with the given capacity."""
    adj[u].append(len(capacity))
    capacity.append([v, cap])
    adj[v].append(len(capacity))
    capacity.append([u, 0])

def bfs(level, adj, capacity, source, sink):
    """Constructs a level graph using BFS."""
    for i in range(len(level)):
        level[i] = -1

    queue = deque([source])
    level[source] = 0

    while queue:
        u = queue.popleft()
        for i in adj[u]:
            v, cap = capacity[i]
            if level[v] == -1 and cap > 0:
                level[v] = level[u] + 1
                queue.append(v)
                if v == sink:
                    return True
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
                capacity[i][1] -= pushed_flow
                capacity[i ^ 1][1] += pushed_flow
                total_flow += pushed_flow
                flow -= pushed_flow
                if flow == 0:
                    break
        ptr[u] += 1
    return total_flow

def dinic_max_flow(n, source, sink, adj, capacity):
    """Computes the maximum flow using Dinic's Algorithm."""
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

def build_network(m, n, preferences):
    """
    Builds the flow network based on the number of patients, doctors, and their preferences.
    
    Parameters:
    - m: Number of patients
    - n: Number of doctors
    - preferences: List of lists, where preferences[i] contains preferred time slots for patient i

    Returns:
    - total_nodes: Total number of nodes in the network
    - source: Source node index
    - sink: Sink node index
    - adj: Adjacency list representing the graph
    - capacity: List representing capacities of the edges
    """
    total_nodes = 1 + m + 3 + n + 1  # source, patients, time slots, doctors, sink
    source, sink = 0, total_nodes - 1

    adj = [[] for _ in range(total_nodes)]
    capacity = []

    # Connect source to patients
    for i in range(m):
        add_edge(adj, capacity, source, i + 1, 1)

    # Connect patients to their preferred time slots
    for i in range(m):
        for time_slot in preferences[i]:
            add_edge(adj, capacity, i + 1, m + time_slot, 1)

    # Connect time slots to doctors
    for time_slot in range(1, 4):
        for j in range(n):
            add_edge(adj, capacity, m + time_slot, m + 4 + j, 1)

    # Connect doctors to sink
    for j in range(n):
        add_edge(adj, capacity, m + 4 + j, sink, 1)

    return total_nodes, source, sink, adj, capacity

def can_all_patients_be_scheduled(m, n, preferences):
    # Build the network
    total_nodes, source, sink, adj, capacity = build_network(m, n, preferences)
    
    # Compute the maximum flow
    max_flow = dinic_max_flow(total_nodes, source, sink, adj, capacity)
    
    return max_flow == m

# Example usage
# m, n = 3, 3
# preferences = [[1, 3], [2, 3], [2, 3]]

# result = can_all_patients_be_scheduled(m, n, preferences)
# print("Yes" if result else "No")  # Expected output: Yes

def test_can_schedule_appointments():
    # 测试用例 1
    m1, n1 = 3, 3
    preferences1 = [[1, 3], [2, 3], [2, 3]]
    assert can_all_patients_be_scheduled(m1, n1, preferences1) == True, "测试用例 1 失败"

    # 测试用例 2
    m2, n2 = 3, 3
    preferences2 = [[1, 3], [2, 3], [1, 2]]
    assert can_all_patients_be_scheduled(m2, n2, preferences2) == True, "测试用例 2 失败"

    # 测试用例 3
    m3, n3 = 4, 3
    preferences3 = [[1, 3], [2, 3], [1, 2], [1, 2]]
    assert can_all_patients_be_scheduled(m3, n3, preferences3) == False, "测试用例 3 失败"

    print("所有测试用例通过！")

# 运行测试用例
test_can_schedule_appointments()