from collections import deque, defaultdict

def bfs(level, graph, source, sink):
    queue = deque([source])
    level[source] = 0
    while queue:
        u = queue.popleft()
        for v, cap, rev in graph[u]:
            if level[v] < 0 and cap > 0:  # Not visited and capacity left
                level[v] = level[u] + 1
                queue.append(v)
                if v == sink:
                    return True
    return False

def dfs(graph, level, ptr, u, sink, flow):
    if u == sink:
        return flow
    while ptr[u] < len(graph[u]):
        v, cap, rev = graph[u][ptr[u]]
        if level[v] == level[u] + 1 and cap > 0:
            curr_flow = min(flow, cap)
            pushed = dfs(graph, level, ptr, v, sink, curr_flow)
            if pushed > 0:
                # Update capacities
                graph[u][ptr[u]][1] -= pushed
                graph[v][rev][1] += pushed
                return pushed
        ptr[u] += 1
    return 0

def dinic_max_flow(n, graph, source, sink):
    total_flow = 0
    while True:
        level = [-1] * n
        if not bfs(level, graph, source, sink):
            break
        ptr = [0] * n
        while True:
            flow = dfs(graph, level, ptr, source, sink, float('inf'))
            if flow == 0:
                break
            total_flow += flow
    return total_flow

def can_assign_patients(A, B, S):
    N = len(A)
    source = N + S
    sink = N + S + 1
    n = N + S + 2
    graph = [[] for _ in range(n)]
    
    # Create edges from source to patients
    for i in range(N):
        graph[source].append([i, 1, len(graph[i])])
        graph[i].append([source, 0, len(graph[source]) - 1])
    
    # Create edges from patients to slots
    for i in range(N):
        a = A[i] - 1
        b = B[i] - 1
        graph[i].append([N + a, 1, len(graph[N + a])])
        graph[N + a].append([i, 0, len(graph[i]) - 1])
        graph[i].append([N + b, 1, len(graph[N + b])])
        graph[N + b].append([i, 0, len(graph[i]) - 1])
    
    # Create edges from slots to sink
    for j in range(S):
        graph[N + j].append([sink, 1, len(graph[sink])])
        graph[sink].append([N + j, 0, len(graph[N + j]) - 1])
    
    max_flow = dinic_max_flow(n, graph, source, sink)
    
    return max_flow == N

def test_can_assign_patients():
    # Boundary Conditions
    assert can_assign_patients([1], [1], 1) == True, "Test Case 1 Failed"  # Single patient and slot
    assert can_assign_patients([1], [2], 2) == True, "Test Case 2 Failed"  # Single patient, multiple slots
    assert can_assign_patients([1, 2], [2, 1], 2) == True, "Test Case 3 Failed"  # Two patients, two slots, each patient can be assigned to a unique slot
    
    # Correctness
    assert can_assign_patients([1, 2, 3], [2, 3, 1], 3) == True, "Test Case 4 Failed"  # Each patient has a slot, possible to assign uniquely
    assert can_assign_patients([1, 1, 2], [2, 3, 3], 3) == True, "Test Case 5 Failed"  # One slot (2) is common but the assignment is possible
    assert can_assign_patients([1, 2, 2, 1], [2, 1, 3, 3], 3) == False, "Test Case 6 Failed"  # Not possible to assign all patients without overlap

    # Performance
    # Large test case with maximum size and feasible assignment
    A = list(range(1, 1001))
    B = list(range(2, 1002))
    assert can_assign_patients(A, B, 1000) == True, "Test Case 7 Failed"

    # Large test case with maximum size but impossible to assign
    A = list(range(1, 1001))
    B = list(range(1, 1001))
    assert can_assign_patients(A, B, 999) == False, "Test Case 8 Failed"

    print("All test cases passed!")

# Run the test method
test_can_assign_patients()