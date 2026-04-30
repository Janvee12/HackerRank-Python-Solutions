# ============================
# PLATFORM:
# HackerRank (Python - Nested Lists / List Comprehension)
# ============================

# ============================
# PROBLEM:
# You are given 4 integers x, y, z, and n.
# You need to print a list of all possible coordinates [i, j, k]
# such that:
#   0 ≤ i ≤ x
#   0 ≤ j ≤ y
#   0 ≤ k ≤ z
# and i + j + k != n
#
# Output should be a list of all valid combinations.
# ============================

# ============================
# APPROACH:
# 1. Use nested loops (or list comprehension).
# 2. Generate all combinations of i, j, k.
# 3. Check condition: i + j + k != n
# 4. Store valid triplets in a list.
# 5. Print final list.
# ============================

# ============================
# TIME COMPLEXITY:
# O(x * y * z)
# Because we generate all possible combinations.
#
# SPACE COMPLEXITY:
# O(x * y * z)
# In worst case, storing all valid triplets.
# ============================

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    data = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]

    print(data)