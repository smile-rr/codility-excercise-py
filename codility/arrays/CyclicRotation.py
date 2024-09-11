def solution(A, K):
    n = len(A)
    
    # 如果数组为空或 K 为 0，则直接返回原数组
    if n == 0 or K == 0:
        return A
    
    # 计算实际需要旋转的次数
    K = K % n
    
    # 使用切片操作实现旋转
    return A[-K:] + A[:-K]

def test_solution():
    # 测试用例 1
    A1 = [3, 8, 9, 7, 6]
    K1 = 3
    assert solution(A1, K1) == [9, 7, 6, 3, 8], f"Test failed for input {A1} with K={K1}"

    # 测试用例 2
    A2 = [0, 0, 0]
    K2 = 1
    assert solution(A2, K2) == [0, 0, 0], f"Test failed for input {A2} with K={K2}"

    # 测试用例 3
    A3 = [1, 2, 3, 4]
    K3 = 4
    assert solution(A3, K3) == [1, 2, 3, 4], f"Test failed for input {A3} with K={K3}"

    # 测试用例 4
    A4 = [1, 2, 3, 4, 5]
    K4 = 2
    assert solution(A4, K4) == [4, 5, 1, 2, 3], f"Test failed for input {A4} with K={K4}"

    # 测试用例 5
    A5 = [1, 2, 3, 4, 5]
    K5 = 7
    assert solution(A5, K5) == [4, 5, 1, 2, 3], f"Test failed for input {A5} with K={K5}"

    # 测试用例 6
    A6 = []
    K6 = 3
    assert solution(A6, K6) == [], f"Test failed for input {A6} with K={K6}"

    print("All tests passed!")

# 运行测试函数
if __name__ == "__main__":
    test_solution()