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

# 示例图
graph = [
    [0, 16, 13, 0, 0, 0],  # 节点 0
    [0, 0, 10, 12, 0, 0],  # 节点 1
    [0, 4, 0, 0, 14, 0],   # 节点 2
    [0, 0, 9, 0, 0, 20],   # 节点 3
    [0, 0, 0, 7, 0, 4],    # 节点 4
    [0, 0, 0, 0, 0, 0]     # 节点 5
]

source = 0  # 源点
sink = 5    # 汇点

# 使用相同的图结构进行测试
print("The maximum possible flow is %d " % edmonds_karp(graph, source, sink))