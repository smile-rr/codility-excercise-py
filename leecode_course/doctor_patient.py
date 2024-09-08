from collections import deque

# 定义 Edmonds-Karp 算法函数
def edmonds_karp(graph, source, sink):
    n = len(graph)
    parent = [-1] * n  # 初始化父节点数组
    max_flow = 0       # 初始化最大流为 0

    # 当存在从源点到汇点的路径时继续
    while bfs(graph, parent, source, sink):
        path_flow = float("Inf")  # 初始化路径上的最小容量为无穷大
        s = sink                  # 从汇点开始回溯
        # 计算路径上的最小容量
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]

        # 更新最大流
        max_flow += path_flow

        # 更新残余网络
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow  # 减少正向边的容量
            graph[v][u] += path_flow  # 增加反向边的容量
            v = parent[v]

    # 返回最大流值
    return max_flow

# 定义广度优先搜索 (BFS) 函数
def bfs(graph, parent, s, t):
    n = len(graph)
    visited = [False] * n  # 初始化访问数组
    queue = deque([s])     # 创建队列并添加源节点
    visited[s] = True      # 标记源节点已访问

    # 当队列不为空时继续
    while queue:
        u = queue.popleft()  # 取出队列中的第一个节点
        # 遍历当前节点的所有邻接节点
        for v in range(n):
            # 如果邻接节点未被访问过且存在剩余容量，则将其加入队列
            if not visited[v] and graph[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
                # 如果到达汇点，则返回 True
                if v == t:
                    return True
    # 如果没有找到从源点到汇点的路径，则返回 False
    return False

# 定义测试函数
def test_patient_doctor_allocation(doctors_capacity, num_patients):
    # 构建图
    # 源点为 0，汇点为最后一个节点
    n = len(doctors_capacity) + 2 + num_patients
    graph = [[0] * n for _ in range(n)]

    # 添加医生到病人的边
    source = 0
    sink = n - 1
    for i, capacity in enumerate(doctors_capacity.values()):
        graph[source][i + 1] = capacity

    # 添加医生到病人的边
    for i in range(len(doctors_capacity)):
        for j in range(num_patients):
            graph[i + 1][len(doctors_capacity) + 1 + j] = 1

    # 求解最大流
    max_flow = edmonds_karp(graph, source, sink)

    # 输出结果
    print(f"The maximum number of patients that can be treated is {max_flow}")

    # 输出具体的分配方案
    allocation = [-1] * num_patients
    for i in range(len(doctors_capacity)):
        for j in range(num_patients):
            if graph[i + 1][len(doctors_capacity) + 1 + j] < 1:
                allocation[j] = i

    print("Patient-Doctor Allocation:")
    for i, doctor in enumerate(allocation):
        print(f"Patient {i} -> Doctor {doctor}")

# 示例数据
doctors_capacity = {
    0: 3,  # 医生 0 可以看 3 个病人
    1: 2,  # 医生 1 可以看 2 个病人
    2: 4   # 医生 2 可以看 4 个病人
}

num_patients = 8

# 调用测试函数
test_patient_doctor_allocation(doctors_capacity, num_patients)