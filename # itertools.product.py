# ============================
# PLATFORM:
# HackerRank (Python - Itertools / itertools.product())
# ============================

# ============================
# PROBLEM:
# Given two lists A and B,
# print their Cartesian Product using itertools.product().
#
# Cartesian Product:
# Every possible pair:
#     (a, b)
# where:
#     a ∈ A
#     b ∈ B
#
# Example:
# Input:
# 1 2
# 3 4
#
# Output:
# (1, 3) (1, 4) (2, 3) (2, 4)
# ============================

# ============================
# APPROACH:
#
# 1. Read two integer lists.
#
# 2. Use itertools.product(A, B)
#    to generate all possible pairs.
#
# 3. Print pairs in required format.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n * m)
#
# n = length of A
# m = length of B
#
# SPACE COMPLEXITY:
# O(1)
# → excluding output
# ============================

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

# Read lists
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

# Generate Cartesian Product
for element in product(A, B):
    print(element, end=' ')