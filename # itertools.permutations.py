# ============================
# PLATFORM:
# HackerRank (Python - Itertools / itertools.permutations())
# ============================

# ============================
# PROBLEM:
# Given a string and an integer k,
# print all possible permutations
# of length k in lexicographic sorted order.
#
# Example:
# Input:
# HACK 2
#
# Output:
# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH
# ============================

# ============================
# APPROACH:
#
# 1. Read input string and integer k.
#
# 2. Sort the string characters
#    to ensure lexicographic order.
#
# 3. Use itertools.permutations()
#    to generate all permutations
#    of length k.
#
# 4. Join tuple characters into string
#    and print.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n! / (n-k)!)
#
# → total permutations generated
#
# SPACE COMPLEXITY:
# O(n! / (n-k)!)
# → storing permutations list
# ============================

from itertools import permutations

# Read input
data, k = input().split()

# Convert k to integer
k = int(k)

# Generate sorted permutations
data = list(permutations(sorted(data), k))

# Print permutations
for item in data:
    print(''.join(item))