# ============================
# PLATFORM:
# HackerRank (Python - Loops)
# ============================

# ============================
# PROBLEM:
# Given an integer n, print the square of all non-negative integers
# less than n.
#
# Example:
# Input: 5
# Output:
# 0
# 1
# 4
# 9
# 16
# ============================

# ============================
# APPROACH:
# 1. Take input integer n.
# 2. Use a loop from 0 to n-1.
# 3. For each number i, print i*i (square of i).
# ============================

# ============================
# TIME COMPLEXITY:
# O(n) → Loop runs n times
#
# SPACE COMPLEXITY:
# O(1) → No extra space used
# ============================

if __name__ == '__main__':
    n = int(input())
    
    for i in range(0, n):
        print(i ** 2)