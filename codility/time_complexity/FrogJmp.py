def solution(X, Y, D):
    # 计算跳跃次数
    jumps = (Y - X + D - 1) // D
    return jumps

def test_solution():
    # 测试用例 1
    X1 = 10
    Y1 = 85
    D1 = 30
    assert solution(X1, Y1, D1) == 3, f"Test failed for input X={X1}, Y={Y1}, D={D1}"

    # 测试用例 2
    X2 = 10
    Y2 = 20
    D2 = 5
    assert solution(X2, Y2, D2) == 2, f"Test failed for input X={X2}, Y={Y2}, D={D2}"

    # 测试用例 3
    X3 = 1
    Y3 = 1000000000
    D3 = 1
    assert solution(X3, Y3, D3) == 999999999, f"Test failed for input X={X3}, Y={Y3}, D={D3}"

    # 测试用例 4
    X4 = 10
    Y4 = 100
    D4 = 10
    assert solution(X4, Y4, D4) == 9, f"Test failed for input X={X4}, Y={Y4}, D={D4}"

    # 测试用例 5
    X5 = 1
    Y5 = 100
    D5 = 10
    assert solution(X5, Y5, D5) == 10, f"Test failed for input X={X5}, Y={Y5}, D={D5}"

    # 打印测试结果
    print("All tests passed!")

# 运行测试函数
if __name__ == "__main__":
    test_solution()