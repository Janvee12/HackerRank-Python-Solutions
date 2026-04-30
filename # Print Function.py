# ============================
# PLATFORM:
# HackerRank (Python - Print Function Problem)
# ============================

# ============================
# PROBLEM:
# Given an integer n, print all numbers from 1 to n in a single line
# without spaces and without newline between numbers.
#
# Example:
# Input: 5
# Output: 12345
# ============================

# ============================
# APPROACH:
# 1. Take input integer n
# 2. Run loop from 1 to n
# 3. Print each number using end=''
#    so numbers appear in same line without space
# ============================

# ============================
# TIME COMPLEXITY:
# O(n) → loop runs n times
#
# SPACE COMPLEXITY:
# O(1) → no extra space used
# ============================

if __name__ == '__main__':
    n = int(input())

    for i in range(1, n + 1):
        print(i, end='')