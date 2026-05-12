# ============================
# PLATFORM:
# HackerRank (Python - Collections / defaultdict Tutorial)
# ============================

# ============================
# PROBLEM:
# You are given two groups of words:
#
# Group A:
# - contains n words
#
# Group B:
# - contains m words
#
# Task:
# For each word in Group B:
# - print positions where it appears in Group A
# - if not found, print -1
#
# Positions are 1-based indexing.
#
# Example:
# Input:
# 5 2
# a
# a
# b
# a
# b
# a
# b
#
# Output:
# 1 2 4
# 3 5
# ============================

# ============================
# APPROACH:
#
# 1. Use defaultdict(list)
#    to store:
#
#       word → list of positions
#
# Example:
# {
#   "a": [1,2,4],
#   "b": [3,5]
# }
#
# 2. Read Group A words
#    and store indices.
#
# 3. For every Group B word:
#    - print stored indices
#    - otherwise print -1
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n + m)
#
# n = words in Group A
# m = queries in Group B
#
# SPACE COMPLEXITY:
# O(n)
# → dictionary storage
# ============================

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict

# Dictionary:
# word -> list of positions
data = defaultdict(list)

# Read sizes
n, m = map(int, input().split())

# ============================
# Read Group A
# ============================
for i in range(1, n + 1):

    word = input()

    data[word].append(str(i))

# ============================
# Process Group B Queries
# ============================
for i in range(m):

    inp = input()

    if inp in data:

        print(" ".join(data[inp]))

    else:
        print(-1)