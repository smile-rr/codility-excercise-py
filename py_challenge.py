def solution(P, Q):
    # 统计两个字符串中相同位置上的相同字符
    same_chars = set()
    # 统计两个字符串中不同位置上的所有字符
    all_chars = set()

    for p_char, q_char in zip(P, Q):
        if p_char == q_char:
            same_chars.add(p_char)
        all_chars.add(p_char)
        all_chars.add(q_char)

    # 最少不同字符数量取决于相同位置上的相同字符数量
    # 如果有相同的字符，优先选择这些字符；如果没有相同的字符，则选择所有不同的字符
    min_distinct_chars = len(same_chars)

    # 如果没有相同的字符，则返回所有不同字符的数量
    if len(same_chars) == 0:
        min_distinct_chars = len(all_chars)

    # 如果相同字符的数量小于所有不同字符的数量，则选择相同字符的数量
    if len(same_chars) < len(all_chars):
        min_distinct_chars = min(min_distinct_chars, len(all_chars) - len(same_chars) + 1)

    return min_distinct_chars

def test_solution():
    # 测试用例 1
    P1 = "abc"
    Q1 = "bcd"
    assert solution(P1, Q1) == 2, f"Test failed for input P={P1}, Q={Q1}"

    # 测试用例 2
    P2 = "axxz"
    Q2 = "yzwy"
    assert solution(P2, Q2) == 2, f"Test failed for input P={P2}, Q={Q2}"

    # 测试用例 3
    P3 = "bacad"
    Q3 = "abada"
    assert solution(P3, Q3) == 1, f"Test failed for input P={P3}, Q={Q3}"

    # 测试用例 4
    P4 = "amz"
    Q4 = "amz"
    assert solution(P4, Q4) == 3, f"Test failed for input P={P4}, Q={Q4}"

    # 测试用例 5
    P5 = "ca"
    Q5 = "ab"
    assert solution(P5, Q5) == 1, f"Test failed for input P={P5}, Q={Q5}"

    # 打印测试结果
    print("All tests passed!")

# 运行测试函数
if __name__ == "__main__":
    test_solution()