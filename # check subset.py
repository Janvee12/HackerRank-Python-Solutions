# ============================
# PLATFORM:
# HackerRank
# (Python - Sets / Check Subset)
# ============================

# ============================
# PROBLEM:
# Given two sets A and B,
# determine whether:
#
#     A ⊆ B
#
# (A is a subset of B)
#
# Print:
# True  -> if every element
#          of A exists in B
#
# False -> otherwise
# ============================

# ============================
# APPROACH:
#
# Python provides:
#
#     setA.issubset(setB)
#
# which directly checks
# whether all elements of
# setA are present in setB.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(len(A))
#
# SPACE COMPLEXITY:
# O(len(A) + len(B))
# ============================

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())

for _ in range(t):

    n_a = int(input())
    val_a = set(map(int, input().split()))

    n_b = int(input())
    val_b = set(map(int, input().split()))

    print(val_a.issubset(val_b))