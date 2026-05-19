# ============================
# PLATFORM:
# HackerRank
# (Python - Itertools / itertools.combinations_with_replacement())
# ============================

# ============================
# PROBLEM:
# Given a string and an integer k,
# print all possible combinations
# of size k with replacement allowed.
#
# Rules:
#
# - Characters must be printed
#   in lexicographic sorted order.
#
# - Repetition is allowed.
#
# Example:
#
# Input:
# HACK 2
#
# Output:
# AA
# AC
# AH
# AK
# CC
# CH
# CK
# HH
# HK
# KK
# ============================

# ============================
# APPROACH:
#
# 1. Read string and integer k.
#
# 2. Sort the string
#    for lexicographic order.
#
# 3. Use:
#
#    combinations_with_replacement()
#
#    from itertools.
#
# 4. Print each combination
#    after joining tuple characters.
#
# ============================

# ============================
# DIFFERENCE:
#
# combinations():
#     no repeated elements
#
# combinations_with_replacement():
#     repeated elements allowed
#
# Example:
#
# combinations('AB',2)
# -> AB
#
# combinations_with_replacement('AB',2)
# -> AA AB BB
# ============================

# ============================
# TIME COMPLEXITY:
#
# O(C(n+k-1, k))
#
# Number of generated combinations.
#
# SPACE COMPLEXITY:
# O(k)
# ============================

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement

# Read input
s, k = input().split()

# Sort characters
s = sorted(s)

# Generate combinations with replacement
for d in combinations_with_replacement(s, int(k)):

    print(''.join(d))