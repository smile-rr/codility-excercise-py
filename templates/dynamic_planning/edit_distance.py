def edit_distance(str1, str2):
    """
    计算两个字符串之间的编辑距离。
    
    参数：
    - str1: 第一个字符串
    - str2: 第二个字符串
    
    返回值：
    - 编辑距离（int）
    """
    m, n = len(str1), len(str2)

    # 创建一个 (m+1) x (n+1) 的二维数组，用于存储子问题的解
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 初始化边界条件
    for i in range(m + 1):
        dp[i][0] = i  # 将 str1 的前 i 个字符删除变成空字符串
    for j in range(n + 1):
        dp[0][j] = j  # 将空字符串插入 j 个字符变成 str2

    # 填充 dp 数组
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]  # 如果字符相同，不需要额外操作
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],    # 删除 str1[i-1]
                                   dp[i][j - 1],    # 插入 str2[j-1]
                                   dp[i - 1][j - 1]) # 替换 str1[i-1] 为 str2[j-1]

    return dp[m][n]

def test_edit_distance():
    # 测试用例 1：相同字符串
    str1, str2 = "kitten", "kitten"
    print(f"Edit distance between '{str1}' and '{str2}' is {edit_distance(str1, str2)}")  # 期望输出: 0

    # 测试用例 2：单个字符的替换
    str1, str2 = "kitten", "sitten"
    print(f"Edit distance between '{str1}' and '{str2}' is {edit_distance(str1, str2)}")  # 期望输出: 1

    # 测试用例 3：插入操作
    str1, str2 = "kitten", "sitting"
    print(f"Edit distance between '{str1}' and '{str2}' is {edit_distance(str1, str2)}")  # 期望输出: 3

    # 测试用例 4：多个字符的替换和删除
    str1, str2 = "flaw", "lawn"
    print(f"Edit distance between '{str1}' and '{str2}' is {edit_distance(str1, str2)}")  # 期望输出: 2

    # 测试用例 5：完全不同的字符串
    str1, str2 = "intention", "execution"
    print(f"Edit distance between '{str1}' and '{str2}' is {edit_distance(str1, str2)}")  # 期望输出: 5

# 运行测试用例
test_edit_distance()