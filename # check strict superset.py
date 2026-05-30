# ============================
# PLATFORM:
# HackerRank
# (Python - Sets / Check Strict Superset)
# ============================

# ============================
# PROBLEM:
# Given a set A and N other sets,
# determine whether:
#
#     A ⊃ B
#
# for every set B.
#
# A is a STRICT SUPERSET if:
#
# 1. Every element of B
#    exists in A.
#
# 2. A and B are not equal.
#
# Print:
#
# True  -> if A is a strict
#          superset of all sets.
#
# False -> otherwise.
# ============================

# ============================
# APPROACH:
#
# Python provides:
#
#     A.issuperset(B)
#
# which checks whether all
# elements of B are present
# in A.
#
# Since we need a STRICT
# superset, we must also
# ensure:
#
#     A != B
#
# If any set fails either
# condition, answer becomes
# False.
# ============================

# ============================
# TIME COMPLEXITY:
#
# O(N × K)
#
# N = number of sets
# K = average size of a set
#
# SPACE COMPLEXITY:
#
# O(max size of set)
# ============================

# Enter your code here. Read input from STDIN. Print output to STDOUT

A = set(map(int, input().split()))

n = int(input())

result = True

for _ in range(n):

    B = set(map(int, input().split()))

    if not (A.issuperset(B) and A != B):

        result = False
        break

print(result)