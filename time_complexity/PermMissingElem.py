def solution(A):
    # 使用高斯求和公式计算 1 到 N+1 的总和
    n = len(A) + 1
    total_sum = n * (n + 1) // 2
    
    # 计算数组 A 中所有元素的总和
    array_sum = sum(A)
    
    # 缺失的元素就是总和减去数组中所有元素的总和
    missing_element = total_sum - array_sum
    return missing_element

def test_solution():
    # 测试用例 1
    A1 = [2, 3, 1, 5]
    assert solution(A1) == 4, f"Test failed for input {A1}"

    # 测试用例 2
    A2 = [1, 2, 3, 4, 6, 7, 8]
    assert solution(A2) == 5, f"Test failed for input {A2}"

    # 测试用例 3
    A3 = [1, 3]
    assert solution(A3) == 2, f"Test failed for input {A3}"

    # 测试用例 4
    A4 = [1, 2, 3, 4, 5, 6, 7, 9]
    assert solution(A4) == 8, f"Test failed for input {A4}"

    # 测试用例 5
    A5 = [1, 2, 4, 5]
    assert solution(A5) == 3, f"Test failed for input {A5}"

    # 打印测试结果
    print("All tests passed!")

# 运行测试函数
if __name__ == "__main__":
    test_solution()