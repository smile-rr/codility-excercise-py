import heapq

def prim_mst(graph):
    """
    使用 Prim 算法计算给定图的最小生成树。
    
    :param graph: 字典表示的带权重图，键是顶点，值是另一个字典，表示与该顶点相连的顶点及其权重
    :return: 最小生成树的总权重和边集
    """
    # 获取顶点数量
    if not graph:
        return 0, []    
    
    # 初始化最小生成树的边集
    mst_edges = []
    
    # 初始化最小生成树的总权重
    mst_weight = 0
    
    # 初始化已访问顶点集合
    visited = set()
    
    # 初始化优先队列，存储未访问顶点及其到已访问顶点的最小权重
    pq = [(0, None, 0)]  # (权重, 上一个顶点, 当前顶点)
    
    while pq:
        weight, prev, current = heapq.heappop(pq)
        
        # 如果当前顶点已被访问，则跳过
        if current in visited:
            continue
        
        # 添加当前顶点到已访问顶点集合
        visited.add(current)
        
        # 更新最小生成树的总权重
        mst_weight += weight
        
        # 添加当前边到最小生成树的边集
        if prev is not None:
            mst_edges.append((prev, current, weight))
        
        # 将当前顶点的邻居加入优先队列
        for neighbor, edge_weight in graph[current].items():
            if neighbor not in visited:
                heapq.heappush(pq, (edge_weight, current, neighbor))
    
    # 处理空图的情况
    if not visited:
        return 0, []
    
    return mst_weight, mst_edges

def test_prim_mst():
    # 测试用例 1：标准图
    graph1 = {
        0: {1: 10, 2: 5},
        1: {2: 2, 3: 1},
        2: {},
        3: {2: 9, 0: 7}
    }
    print(f"Test Case 1: {graph1}")
    result1 = prim_mst(graph1)
    print(f"Result: {result1}")
    assert result1 == (16, [(0, 2, 5), (0, 1, 10),(1, 3, 1)])  # 预期结果包含边和权重

    # 测试用例 2：空图
    graph2 = {}
    print(f"Test Case 2: {graph2}")
    result2 = prim_mst(graph2)
    print(f"Result: {result2}")
    assert result2 == (0, [])

    # 测试用例 3：只有一个顶点的图
    graph3 = {0: {}}
    print(f"Test Case 3: {graph3}")
    result3 = prim_mst(graph3)
    print(f"Result: {result3}")
    assert result3 == (0, [])

    # 测试用例 4：包含孤立顶点的图
    graph4 = {
        0: {1: 10},
        1: {0: 10},
        2: {}
    }
    print(f"Test Case 4: {graph4}")
    result4 = prim_mst(graph4)
    print(f"Result: {result4}")
    assert result4 == (10, [(0, 1, 10)])

    # 测试用例 5：所有顶点相互连接的图
    graph5 = {
        0: {1: 1, 2: 1},
        1: {0: 1, 2: 1},
        2: {0: 1, 1: 1}
    }
    print(f"Test Case 5: {graph5}")
    result5 = prim_mst(graph5)
    print(f"Result: {result5}")
    assert result5 == (2, [(0, 1, 1), (0, 2, 1)])

test_prim_mst()