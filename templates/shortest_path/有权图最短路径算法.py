import heapq

def dijkstra(graph, start, end):
    """
    使用 Dijkstra 算法计算有权图的最短路径，并记录最短路径经过的顶点。
    
    :param graph: 字典表示的有权图，键是顶点，值是邻接表，每个元素为 (邻居, 权重) 的元组
    :param start: 起始顶点
    :param end: 目标顶点
    :return: 到达目标顶点的最短路径长度和最短路径经过的顶点列表，如果不存在路径则返回 -1 和空列表
    """
    # 初始化距离字典，将所有顶点的距离设为无穷大
    distance = {vertex: float('inf') for vertex in graph}
    distance[start] = 0
    
    # 初始化前驱节点字典
    previous = {vertex: None for vertex in graph}
    
    # 初始化优先队列，将起始顶点入队
    priority_queue = [(0, start)]
    
    while priority_queue:
        # 弹出当前距离最小的顶点
        current_distance, current = heapq.heappop(priority_queue)
        
        # 如果当前顶点到目标顶点的距离更小，直接返回
        if current == end:
            return distance[end], reconstruct_path(previous, start, end)
        
        # 遍历当前顶点的所有邻居
        for neighbor, weight in graph[current]:
            new_distance = current_distance + weight
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                previous[neighbor] = current
                heapq.heappush(priority_queue, (new_distance, neighbor))
                
    return -1, []

def reconstruct_path(previous, start, end):
    """
    从目标顶点回溯到起始顶点，得到最短路径。
    
    :param previous: 前驱节点字典
    :param start: 起始顶点
    :param end: 目标顶点
    :return: 最短路径经过的顶点列表
    """
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous[current]
    path.reverse()  # 反转路径
    return path

# 示例图
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

def test_dijkstra():
    print("Testing Dijkstra algorithm...")
    dist, path = dijkstra(graph, 'A', 'D')
    assert dist == 4 and path == ['A', 'B', 'C', 'D'], "Test case 1 failed"
    
    dist, path = dijkstra(graph, 'B', 'D')
    assert dist == 3 and path == ['B', 'C', 'D'], "Test case 2 failed"
    
    dist, path = dijkstra(graph, 'C', 'D')
    assert dist == 1 and path == ['C', 'D'], "Test case 3 failed"
    
    dist, path = dijkstra(graph, 'D', 'A')
    assert dist == 4 and path == ['D', 'C', 'B', 'A'], "Test case 4 failed"
    
    dist, path = dijkstra(graph, 'A', 'A')
    assert dist == 0 and path == ['A'], "Test case 5 failed"
    
    dist, path = dijkstra(graph, 'D', 'E')
    assert dist == -1 and path == [], "Test case 6 failed"  # 不存在的顶点 E
    print("All test cases passed!")

# 运行测试
test_dijkstra()