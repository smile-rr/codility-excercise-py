def floyd_warshall(graph):
    """
    使用 Floyd-Warshall 算法计算所有顶点对之间的最短路径。
    
    :param graph: 字典表示的带权重图，键是顶点，值是另一个字典，表示与该顶点相连的顶点及其权重
    :return: 一个二维列表，其中 dist[i][j] 表示从顶点 i 到顶点 j 的最短路径长度
    """
    # 获取顶点数量
    num_vertices = len(graph)
    
    # 初始化距离矩阵
    dist = [[float('inf')] * num_vertices for _ in range(num_vertices)]
    
    # 设置对角线上的距离为 0
    for i in range(num_vertices):
        dist[i][i] = 0
    
    # 设置初始距离
    for u in graph:
        for v, weight in graph[u].items():
            dist[u][v] = weight
    
    # 动态规划求解最短路径
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

# 示例图
graph = {
    0: {1: 10, 2: 5},
    1: {2: 2, 3: 1},
    2: {},
    3: {2: 9, 0: 7}
}

# 计算最短路径
dist = floyd_warshall(graph)

# 输出结果
print("Distance matrix:")
for row in dist:
    print(row)