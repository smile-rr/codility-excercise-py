def longest_common_subsequence(str1, str2):
    """
    计算两个字符串的最长公共子序列（LCS）的长度。

    参数：
    - str1: 第一个字符串
    - str2: 第二个字符串

    返回值：
    - LCS 的长度（int）
    """
    m, n = len(str1), len(str2)

    # 创建一个 (m+1) x (n+1) 的二维数组，初始化为 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 填充 dp 数组
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                # 如果字符相同，则当前 LCS 长度为前一个 LCS 长度加 1
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # 如果字符不相同，则取前一个子问题的最大值
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

def test_lcs():
    # 测试用例 1：完全相同的字符串
    str1, str2 = "abcde", "abcde"
    print(f"LCS of '{str1}' and '{str2}' is {longest_common_subsequence(str1, str2)}")  # 期望输出: 5

    # 测试用例 2：部分相同的字符串
    str1, str2 = "abc", "ac"
    print(f"LCS of '{str1}' and '{str2}' is {longest_common_subsequence(str1, str2)}")  # 期望输出: 2

    # 测试用例 3：没有公共子序列的字符串
    str1, str2 = "abc", "def"
    print(f"LCS of '{str1}' and '{str2}' is {longest_common_subsequence(str1, str2)}")  # 期望输出: 0

    # 测试用例 4：一个字符串是另一个的子串
    str1, str2 = "abcdef", "ace"
    print(f"LCS of '{str1}' and '{str2}' is {longest_common_subsequence(str1, str2)}")  # 期望输出: 3

    # 测试用例 5：重复字符的字符串
    str1, str2 = "aaaa", "aa"
    print(f"LCS of '{str1}' and '{str2}' is {longest_common_subsequence(str1, str2)}")  # 期望输出: 2

# 运行测试用例
test_lcs()