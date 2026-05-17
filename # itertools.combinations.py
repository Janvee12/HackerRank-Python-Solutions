# ============================
# PLATFORM:
# HackerRank (Python - Itertools / itertools.combinations())
# ============================

# ============================
# PROBLEM:
# Given a string and an integer r,
# print all combinations of the string
# for lengths from 1 to r.
#
# Output combinations in:
# - lexicographic order
# - increasing combination length
#
# Example:
#
# Input:
# HACK 2
#
# Output:
# A
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK
# ============================

# ============================
# APPROACH:
#
# 1. Read string and integer r.
#
# 2. Sort the string
#    for lexicographic order.
#
# 3. Generate combinations
#    for sizes:
#
#       1 → r
#
# 4. Print every combination
#    by joining tuple characters.
#
# ============================

# ============================
# TIME COMPLEXITY:
#
# O(total combinations)
#
# Total combinations:
#
# C(n,1) + C(n,2) + ... + C(n,r)
#
# SPACE COMPLEXITY:
# O(r)
# → temporary combination storage
# ============================

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

# Read input
data, r = input().split()

# Sort characters
data = sorted(data)

# Convert r to integer
r = int(r)

# Generate combinations
for i in range(1, r + 1):

    combo = combinations(data, i)

    for c in combo:

        print(''.join(c))