# ============================
# PLATFORM:
# HackerRank
# (Python - Itertools / Compress the String!)
# ============================

# ============================
# PROBLEM:
# Given a string of digits,
# compress consecutive repeated digits
# into tuples:
#
#     (count, digit)
#
# Example:
#
# Input:
# 1222311
#
# Output:
# (1, 1) (3, 2) (1, 3) (2, 1)
# ============================

# ============================
# APPROACH:
#
# Use itertools.groupby()
#
# groupby():
# groups consecutive identical elements.
#
# Example:
#
# "1222311"
#
# groups:
# 1
# 222
# 3
# 11
#
# For each group:
#
# - count occurrences
# - print:
#
#       (count, digit)
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
#
# SPACE COMPLEXITY:
# O(n)
# ============================

# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import groupby

# Create compressed result
result = [

    (len(list(c)), int(k))

    for k, c in groupby(input())
]

# Print tuples
print(*result)