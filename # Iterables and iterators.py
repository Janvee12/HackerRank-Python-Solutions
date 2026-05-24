# ============================
# PLATFORM:
# HackerRank
# (Python - Itertools / Iterables and Iterators)
# ============================

# ============================
# PROBLEM:
# Given:
#
# - a list of lowercase letters
# - an integer k
#
# Task:
# Find the probability that
# at least one selected index
# contains the letter 'a'
# when choosing k elements.
#
# Example:
#
# Input:
# 4
# a a c d
# 2
#
# Output:
# 0.8333
# ============================

# ============================
# APPROACH:
#
# 1. Generate all combinations
#    of size k.
#
# 2. Count combinations
#    containing letter 'a'.
#
# 3. Probability:
#
#       favorable / total
#
# ============================

# ============================
# TIME COMPLEXITY:
#
# O(C(n, k))
#
# SPACE COMPLEXITY:
# O(C(n, k))
# ============================

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations

# Input size (not used directly)
n = input()

# List of characters
l = input().split()

# Combination size
m = int(input())

# Count favorable combinations
count = 0

# Generate all combinations
all_combinations = list(combinations(l, m))

for i in all_combinations:

    # Check if 'a' exists
    if 'a' in i:

        count += 1

# Print probability
print(count / len(all_combinations))