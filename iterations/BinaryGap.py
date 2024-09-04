def solution(N):
    binary_str = bin(N)[2:]
    max_gap_length = 0
    current_gap_length = 0
    
    found_first_one = False  # 标记是否已经找到第一个 '1'
    
    for bit in binary_str:
        if bit == '1':
            if found_first_one:
                max_gap_length = max(max_gap_length, current_gap_length)
            current_gap_length = 0
            found_first_one = True
        elif found_first_one and bit == '0':
            current_gap_length += 1
    
    return max_gap_length

def test_solution():
    # 基本测试用例
    assert solution(9) == 2  # 1001
    assert solution(529) == 4  # 1000010001
    assert solution(20) == 1  # 10100
    assert solution(15) == 0  # 1111
    assert solution(32) == 0  # 100000
    
    # 边界测试用例
    assert solution(1) == 0  # 1
    assert solution(2147483647) == 0  # 1111111111111111111111111111111
    
    # 特殊情况
    assert solution(1041) == 5  # 10000010001
    assert solution(32768) == 0  # 1000000000000000
    assert solution(2147483646) == 0  # 1111111111111111111111111111110
    
    # 多个二进制间隙的情况
    assert solution(2147483645) == 1 # 1111111111111111111111111111101
    assert solution(1073741825) == 29  # 1000000000000000000000000000001
    
    print("All tests passed!")

# 运行测试函数
test_solution()