def solution(A):
    result = 0
    
    # 遍历数组中的所有元素
    for num in A:
        result ^= num  # 对每个元素进行异或操作
    
    return result  # 返回最终结果

def test_solution():
    # 测试用例 1
    A1 = [9, 3, 9, 3, 9, 7, 9]
    assert solution(A1) == 7, f"Test failed for input {A1}"

    # 测试用例 2
    A2 = [1, 5, 2, 2, 3, 3, 1, 5]
    assert solution(A2) == 0, f"Test failed for input {A2}"  # 0 表示未配对的元素不存在

    # 测试用例 3
    A3 = [4, 4, 2, 2, 1]
    assert solution(A3) == 1, f"Test failed for input {A3}"

    # 打印测试结果
    print("All tests passed!")

# 运行测试函数
if __name__ == "__main__":
    test_solution()