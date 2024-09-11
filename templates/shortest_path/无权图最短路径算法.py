from collections import deque

def bfs_shortest_path(graph, start, end):
    """
    使用 BFS 算法计算无权图的最短路径，并记录最短路径经过的顶点。
    
    :param graph: 字典表示的无向图，键是顶点，值是相邻顶点列表
    :param start: 起始顶点
    :param end: 目标顶点
    :return: 到达目标顶点的最短路径长度和最短路径经过的顶点列表，如果不存在路径则返回 -1 和空列表
    """
    # 初始化距离字典，将所有顶点的距离设为无穷大
    distance = {vertex: float('inf') for vertex in graph}
    distance[start] = 0
    
    # 初始化前驱节点字典
    previous = {vertex: None for vertex in graph}
    
    # 初始化队列，将起始顶点入队
    queue = deque([start])
    
    # 初始化已访问集合
    visited = set()
    
    while queue:
        current = queue.popleft()
        
        # 如果当前顶点是目标顶点，直接返回距离和路径
        if current == end:
            return distance[end], reconstruct_path(previous, start, end)
        
        # 标记当前顶点为已访问
        visited.add(current)
        
        # 遍历当前顶点的所有邻居
        for neighbor in graph[current]:
            if neighbor not in visited and distance[neighbor] == float('inf'):
                distance[neighbor] = distance[current] + 1
                previous[neighbor] = current
                queue.append(neighbor)
                
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
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# 测试函数
def test_bfs_shortest_path():
    print("Testing BFS shortest path algorithm...")
    dist, path = bfs_shortest_path(graph, 'A', 'E')
    assert dist == 2 and path == ['A', 'B', 'E'], "Test case 1 failed"
    
    dist, path = bfs_shortest_path(graph, 'A', 'D')
    assert dist == 2 and path == ['A', 'B', 'D'], "Test case 2 failed"
    
    dist, path = bfs_shortest_path(graph, 'A', 'F')
    assert dist == 2 and path == ['A', 'C', 'F'], "Test case 3 failed"
    
    dist, path = bfs_shortest_path(graph, 'D', 'F')
    assert dist == 3 and path == ['D', 'B', 'E', 'F'], "Test case 4 failed"
    
    dist, path = bfs_shortest_path(graph, 'E', 'C')
    print(f"Distance: {dist}, Path: {path}")
    assert dist == 2 and path == ['E', 'F', 'C'], "Test case 5 failed"
    
    dist, path = bfs_shortest_path(graph, 'F', 'A')
    assert dist == 2 and path == ['F', 'C', 'A'], "Test case 6 failed"
    
    dist, path = bfs_shortest_path(graph, 'D', 'G')
    assert dist == -1 and path == [], "Test case 7 failed"  # 不存在的顶点 G
    print("All test cases passed!")

# 运行测试
test_bfs_shortest_path()