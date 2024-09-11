import random
import time
def count_lowercase_before_uppercase(letters):
    n = len(letters)
    
    # Initialize dp array with high values
    dp = [float('inf')] * (n + 1)
    dp[0] = 0  # No cost at the start
    
    # Dictionary to keep track of counts of lowercase letters
    lowercase_count = {}
    total_count = 0
    
    # Traverse the string
    for i in range(n):
        char = letters[i]
        
        if 'a' <= char <= 'z':  # Lowercase letter
            if char not in lowercase_count:
                lowercase_count[char] = 0
            lowercase_count[char] += 1
        
        elif 'A' <= char <= 'Z':  # Uppercase letter
            lowercase_char = char.lower()
            if lowercase_char in lowercase_count:
                total_count += lowercase_count[lowercase_char]
    
    return total_count

def run_tests():
    # Original Test Cases
    print("Original Test Cases:")
    print(f"Test Case 1 (aaAbcCABBc): {count_lowercase_before_uppercase('aaAbcCABBc')}")  # Expected output: 2
    print(f"Test Case 2 (xyzXYabcABC): {count_lowercase_before_uppercase('xyzXYabcABC')}")  # Expected output: 6
    print(f"Test Case 3 (ABCabcAefG): {count_lowercase_before_uppercase('ABCabcAefG')}")  # Expected output: 0

    # Boundary Cases
    print("\nBoundary Cases:")
    print(f"Empty String: {count_lowercase_before_uppercase('')}")  # Expected output: 0
    print(f"Single Lowercase: {count_lowercase_before_uppercase('a')}")  # Expected output: 0
    print(f"Single Uppercase: {count_lowercase_before_uppercase('A')}")  # Expected output: 0
    print(f"Two Characters Lowercase Followed by Uppercase: {count_lowercase_before_uppercase('aA')}")  # Expected output: 1
    print(f"Two Characters Uppercase Followed by Lowercase: {count_lowercase_before_uppercase('Aa')}")  # Expected output: 0

    # Special Cases
    print("\nSpecial Cases:")
    print(f"Consecutive Lowercase and Uppercase Pairs: {count_lowercase_before_uppercase('aAbBcCdD')}")  # Expected output: 4
    print(f"Lowercase Letters Followed by Uppercase Letters: {count_lowercase_before_uppercase('abcABC')}")  # Expected output: 3
    print(f"Interleaved Uppercase and Lowercase Letters: {count_lowercase_before_uppercase('aAbBcCdD')}")  # Expected output: 4

    # Performance Test Case
    print("\nPerformance Test Case:")
    N = 1000000
    # Create a large input with a repeating pattern
    large_input = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', k=N))
    
    start_time = time.time()
    min_val = count_lowercase_before_uppercase(large_input)
    end_time = time.time()
    
    print(f"Min val: {min_val}")
    print(f"Time taken: {end_time - start_time} seconds")

# Run all test cases
run_tests()