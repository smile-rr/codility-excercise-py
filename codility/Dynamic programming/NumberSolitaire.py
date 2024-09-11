def solution(A):
    N = len(A)
    dp = [-float('inf')] * N
    dp[0] = A[0]

    for i in range(N):
        if dp[i] == -float('inf'):
            continue  # 跳过不可达的方格
        
        for dice in range(1, 7):  # 骰子掷出的结果从 1 到 6
            next_pos = i + dice
            if next_pos < N:
                dp[next_pos] = max(dp[next_pos], dp[i] + A[next_pos])

    return dp[N - 1]

def test_solution():
    # 测试用例 1：示例用例
    A = [1, -2, 0, 9, -1, -2]
    print(f"Max result: {solution(A)}")  # 期望输出: 8

    # 测试用例 2：全是正数
    A = [1, 2, 3, 4, 5, 6]
    print(f"Max result: {solution(A)}")  # 期望输出: 21

    # 测试用例 3：全是负数
    A = [-1, -2, -3, -4, -5, -6]
    print(f"Max result: {solution(A)}")  # 期望输出: -1

    # 测试用例 4：有零值
    A = [1, -2, 0, 0, 3, 4]
    print(f"Max result: {solution(A)}")  # 期望输出: 8

    # 测试用例 5：只有两个方格
    A = [5, -3]
    print(f"Max result: {solution(A)}")  # 期望输出: 2

    # 测试用例 6：随机值
    A = [1, 2, -1, -4, 3, 2, 1]
    print(f"Max result: {solution(A)}")  # 期望输出: 7

# 运行测试用例
test_solution()