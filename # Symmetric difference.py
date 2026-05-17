# ============================
# PLATFORM:
# HackerRank (Python - Sets / Symmetric Difference)
# ============================

# ============================
# PROBLEM:
# You are given two sets of integers.
#
# Task:
# Print the symmetric difference
# of the two sets in ascending order.
#
# Symmetric Difference:
#
# Elements present in either set,
# but NOT in both.
#
# Example:
#
# Set A = {2, 4, 5, 9}
# Set B = {2, 4, 11, 12}
#
# Symmetric Difference:
# {5, 9, 11, 12}
# ============================

# ============================
# APPROACH:
#
# 1. Read both sets.
#
# 2. Find:
#
#    - Union:
#          all unique elements
#
#    - Intersection:
#          common elements
#
# 3. Symmetric Difference:
#
#       union - intersection
#
# 4. Sort result and print.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n log n)
#
# - Set operations: O(n)
# - Sorting: O(n log n)
#
# SPACE COMPLEXITY:
# O(n)
# ============================

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Read first set
m = int(input())

minp = set(map(int, input().split()))

# Read second set
n = int(input())

ninp = set(map(int, input().split()))

# Union of sets
data = minp.union(ninp)

# Common elements
common = minp.intersection(ninp)

# Print symmetric difference
for i in sorted(data.difference(common)):

    print(i)