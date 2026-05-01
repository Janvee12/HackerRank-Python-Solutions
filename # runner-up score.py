# ============================
# PLATFORM:
# HackerRank (Python - Basic Data Structures)
# ============================

# ============================
# PROBLEM (Runner-Up Score):
# Given a list of integers, find the second highest (runner-up) score.
#
# Constraints:
# - List may contain duplicate values
# - You must find the second distinct maximum value
#
# Example:
# Input:
# 5
# 2 3 6 6 5
#
# Output:
# 5
# ============================

# ============================
# APPROACH:
# 1. Read input values.
# 2. Find the maximum value (mx).
# 3. Traverse the list again:
#    - Find the largest value smaller than mx.
# 4. Print the second maximum (runner-up).
#
# Note:
# We avoid sorting to keep it efficient.
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
# → One pass to find max + one pass to find second max
#
# SPACE COMPLEXITY:
# O(1)
# → No extra space used
# ============================

if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]

    # Step 1: Find maximum
    mx = arr[0]
    for score in arr:
        if score > mx:
            mx = score

    # Step 2: Find second maximum (runner-up)
    sm = -101   # given constraints (scores ≥ -100)
    for score in arr:
        if score > sm and score < mx:
            sm = score

    print(sm)