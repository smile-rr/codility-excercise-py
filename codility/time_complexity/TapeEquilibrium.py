def solution(A):
    # 计算整个数组的总和
    total_sum = sum(A)
    
    # 初始化左边部分的总和为 0
    left_sum = 0
    
    # 初始化最小差异为正无穷
    min_diff = float('inf')
    
    # 遍历数组，计算每种分割方式下的差异
    for i in range(len(A) - 1):
        left_sum += A[i]
        right_sum = total_sum - left_sum
        diff = abs(left_sum - right_sum)
        
        # 更新最小差异
        if diff < min_diff:
            min_diff = diff
            
    return min_diff

def test_solution():
    # 测试用例 1
    A1 = [3, 1, 2, 4, 3]
    assert solution(A1) == 1, f"Test failed for input {A1}"

    # 测试用例 2
    A2 = [1, 2, 3, 4, 5]
    assert solution(A2) == 3, f"Test failed for input {A2}"

    # 测试用例 3
    A3 = [-1000, 1000]
    assert solution(A3) == 2000, f"Test failed for input {A3}"

    # 测试用例 4
    A4 = [1, -1, 1, -1, 1]
    assert solution(A4) == 1, f"Test failed for input {A4}"

    # 测试用例 5
    A5 = [1, 1, 1, 1, 1, 1]
    assert solution(A5) == 0, f"Test failed for input {A5}"

    # 打印测试结果
    print("All tests passed!")

# 运行测试函数
if __name__ == "__main__":
    test_solution()