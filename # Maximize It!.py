# ============================
# PLATFORM:
# HackerRank
# (Python - Itertools / Maximize It!)
# ============================

# ============================
# PROBLEM:
# You are given:
#
#     K lists
#     and integer M
#
# Choose exactly one element
# from each list such that:
#
#     S = (sum(x^2)) % M
#
# is maximized.
#
# Task:
# Print the maximum possible value.
#
# Example:
#
# Input:
# 3 1000
# 2 5 4
# 3 7 8 9
# 5 5 7 8 9 10
#
# Output:
# 206
# ============================

# ============================
# APPROACH:
#
# Use itertools.product()
#
# product(*lists)
# generates all possible selections
# taking one element from each list.
#
# For every combination:
#
# 1. Compute:
#
#       sum(x*x for x in combination)
#
# 2. Take modulo M
#
# 3. Track maximum value.
#
# ============================

# ============================
# TIME COMPLEXITY:
#
# O(product of list sizes)
#
# SPACE COMPLEXITY:
# O(1)
# excluding generated tuples
# ============================

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

# Read K and M
n, m = [int(x) for x in input().split()]

# Store lists
l1 = []

for i in range(n):

    # Ignore first number
    # because it represents list length
    l = list(map(int, input().split()))[1:]

    l1.append(l)

# Compute all possible values
r = map(

    lambda x:
    sum(i * i for i in x) % m,

    product(*l1)
)

# Print maximum result
print(max(r))