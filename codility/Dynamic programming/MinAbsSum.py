import random
import time
def solution(A):
    total_sum = sum(A)
    
    # If total_sum is 0, the result is obviously 0
    if total_sum == 0:
        return 0
    
    target = total_sum // 2

    # Ensure target is non-negative
    if target < 0:
        target = 0

    # Dynamic Programming array
    dp = [False] * (target + 1)
    dp[0] = True

    for num in A:
        if num > 0:
            # Update dp array for positive numbers
            for j in range(target, num - 1, -1):
                if dp[j - num]:
                    dp[j] = True
        elif num < 0:
            # Update dp array for negative numbers
            num = -num
            for j in range(target - num + 1):
                if dp[j]:
                    dp[j + num] = True

    # Find the closest sum to target
    for s in range(target, -1, -1):
        if dp[s]:
            return abs(total_sum - 2 * s)

# Test cases
def test_cases():
    # Simple Cases
    A1 = [1, 5, 2, -2]
    A2 = [1, 2, 3, 4, 5]
    A3 = [-1, -2, -3, -4, -5]
    
    print(f"Simple Case 1 Min val: {solution(A1)}")  # Expected output: 0
    print(f"Simple Case 2 Min val: {solution(A2)}")  # Expected output: 1
    print(f"Simple Case 3 Min val: {solution(A3)}")  # Expected output: 1
    
    # Boundary Cases
    A4 = [7]
    A5 = [5, 3]
    A6 = []
    
    print(f"Boundary Case 1 Min val: {solution(A4)}")  # Expected output: 7
    print(f"Boundary Case 2 Min val: {solution(A5)}")  # Expected output: 1 or 2
    print(f"Boundary Case 3 Min val: {solution(A6)}")  # Expected output: 0
    
    # Medium Cases
    A7 = [1, -1, 2, -2, 3, -3, 4, -4, 5, -5]
    A8 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    print(f"Medium Case 1 Min val: {solution(A7)}")  # Expected output: 0
    print(f"Medium Case 2 Min val: {solution(A8)}")  # Expected output: 0 or other minimal value
    
    # Large Number Test Case
    N = 20000
    A9 = [random.randint(-100, 100) for _ in range(N)]
    
    start_time = time.time()
    min_val = solution(A9)
    end_time = time.time()
    
    print(f"Large Number Test Min val: {min_val}")
    print(f"Time taken: {end_time - start_time} seconds")

# Run all test cases
test_cases()