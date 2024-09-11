def bpm(u, matchR, seen, adj):
    """
    使用DFS查找增广路径，尝试为左部集合中的一个顶点u匹配一个右部集合中的顶点。
    
    Parameters:
    - u: 当前正在尝试匹配的左部集合顶点
    - matchR: 右部集合顶点的匹配状态
    - seen: 右部集合顶点的访问状态
    - adj: 邻接表，表示二分图的连接关系

    Returns:
    - bool: 如果找到增广路径返回True，否则返回False
    """
    for v in adj[u]:
        if not seen[v]:
            seen[v] = True  # 标记为访问过

            # 如果v没有匹配或可以找到增广路径
            if matchR[v] == -1 or bpm(matchR[v], matchR, seen, adj):
                matchR[v] = u  # 为v匹配u
                return True
    return False

def hungarian_algorithm(n, m, adj):
    """
    使用匈牙利算法在二分图中找到最大匹配。
    
    Parameters:
    - n: 左部集合的顶点数
    - m: 右部集合的顶点数
    - adj: 邻接表，表示二分图的连接关系

    Returns:
    - int: 最大匹配数
    """
    matchR = [-1] * m  # 右部集合顶点的匹配状态，初始化为未匹配
    result = 0

    for u in range(n):
        seen = [False] * m  # 右部集合顶点的访问状态
        if bpm(u, matchR, seen, adj):
            result += 1

    return result

# 测试用例
n = 4  # 左部集合顶点数
m = 4  # 右部集合顶点数

# 邻接表表示二分图的连接关系
adj = [
    [0, 1],     # 左部集合的顶点 0 连接到右部集合的顶点 0, 1
    [1, 2],     # 左部集合的顶点 1 连接到右部集合的顶点 1, 2
    [0, 2],     # 左部集合的顶点 2 连接到右部集合的顶点 0, 2
    [2, 3]      # 左部集合的顶点 3 连接到右部集合的顶点 2, 3
]

# 计算最大匹配数
max_matching = hungarian_algorithm(n, m, adj)
print("The maximum matching is:", max_matching)