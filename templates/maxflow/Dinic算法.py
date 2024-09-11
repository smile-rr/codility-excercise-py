from collections import defaultdict

def add_edge(adj_list, capacity, u, v, cap):
    forward = (v, cap, len(adj_list[v]))
    reverse = (u, 0, len(adj_list[u]))
    adj_list[u].append(forward)
    adj_list[v].append(reverse)
    capacity[u, v] = cap

def bfs(adj_list, capacity, level, source, sink):
    num_vertices = len(adj_list)
    for i in range(num_vertices):
        level[i] = -1
    queue = [source]
    level[source] = 0
    while queue:
        u = queue.pop(0)
        for v, cap, _ in adj_list[u]:
            if cap > 0 and level[v] < 0:
                level[v] = level[u] + 1
                queue.append(v)
    return level[sink] != -1

def dfs(adj_list, capacity, level, working, u, sink, flow):
    if u == sink:
        return flow
    while working[u] < len(adj_list[u]):
        v, cap, rev = adj_list[u][working[u]]
        if cap > 0 and level[u] < level[v]:
            new_flow = dfs(adj_list, capacity, level, working, v, sink, min(flow, cap))
            if new_flow > 0:
                capacity[u, v] -= new_flow
                capacity[v, u] += new_flow
                return new_flow
        working[u] += 1
    return 0

def dinic_max_flow(num_vertices, adj_list, capacity, source, sink):
    max_flow = 0
    level = [0] * num_vertices
    working = [0] * num_vertices
    
    while bfs(adj_list, capacity, level, source, sink):
        for i in range(num_vertices):
            working[i] = 0
        while True:
            flow = dfs(adj_list, capacity, level, working, source, sink, float('inf'))
            if flow == 0:
                break
            max_flow += flow
    return max_flow

def test_dinic():
    # 测试用例 1：标准图
    num_vertices = 6
    adj_list = defaultdict(list)
    capacity = defaultdict(int)
    add_edge(adj_list, capacity, 0, 1, 16)
    add_edge(adj_list, capacity, 0, 2, 13)
    add_edge(adj_list, capacity, 1, 2, 10)
    add_edge(adj_list, capacity, 1, 3, 12)
    add_edge(adj_list, capacity, 2, 1, 4)
    add_edge(adj_list, capacity, 2, 4, 14)
    add_edge(adj_list, capacity, 3, 2, 9)
    add_edge(adj_list, capacity, 3, 5, 20)
    add_edge(adj_list, capacity, 4, 3, 7)
    add_edge(adj_list, capacity, 4, 5, 4)
    
    max_flow = dinic_max_flow(num_vertices, adj_list, capacity, 0, 5)
    print("测试用例 1：标准图")
    print("最大流值:", max_flow)
    assert max_flow == 23

    # 测试用例 2：空图
    num_vertices = 0
    adj_list = defaultdict(list)
    capacity = defaultdict(int)
    max_flow = dinic_max_flow(num_vertices, adj_list, capacity, 0, 0)
    print("测试用例 2：空图")
    print("最大流值:", max_flow)
    assert max_flow == 0

    # 测试用例 3：只有一个顶点的图
    num_vertices = 1
    adj_list = defaultdict(list)
    capacity = defaultdict(int)
    max_flow = dinic_max_flow(num_vertices, adj_list, capacity, 0, 0)
    print("测试用例 3：只有一个顶点的图")
    print("最大流值:", max_flow)
    assert max_flow == 0

    # 测试用例 4：包含孤立顶点的图
    num_vertices = 3
    adj_list = defaultdict(list)
    capacity = defaultdict(int)
    add_edge(adj_list, capacity, 0, 1, 10)
    add_edge(adj_list, capacity, 1, 0, 10)
    max_flow = dinic_max_flow(num_vertices, adj_list, capacity, 0, 2)
    print("测试用例 4：包含孤立顶点的图")
    print("最大流值:", max_flow)
    assert max_flow == 0

    # 测试用例 5：所有顶点相互连接的图
    num_vertices = 4
    adj_list = defaultdict(list)
    capacity = defaultdict(int)
    add_edge(adj_list, capacity, 0, 1, 1)
    add_edge(adj_list, capacity, 0, 2, 1)
    add_edge(adj_list, capacity, 1, 2, 1)
    add_edge(adj_list, capacity, 1, 3, 1)
    add_edge(adj_list, capacity, 2, 3, 1)
    max_flow = dinic_max_flow(num_vertices, adj_list, capacity, 0, 3)
    print("测试用例 5：所有顶点相互连接的图")
    print("最大流值:", max_flow)
    assert max_flow == 2

test_dinic()