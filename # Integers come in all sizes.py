# ============================
# PLATFORM:
# HackerRank
# (Python - Integers Come In All Sizes)
# ============================

# ============================
# PROBLEM:
# Given four integers:
#
#     a
#     b
#     c
#     d
#
# Compute:
#
#     (a^b) + (c^d)
#
# and print the result.
#
# Example:
#
# Input:
# 9
# 29
# 7
# 27
#
# Output:
# 4710194409608608369201743232
# ============================

# ============================
# APPROACH:
#
# Use exponentiation operator:
#
#     **
#
# Python supports
# arbitrarily large integers,
# so very large values
# can be handled directly.
#
# ============================

# ============================
# TIME COMPLEXITY:
#
# Fast exponentiation:
# O(log b + log d)
#
# SPACE COMPLEXITY:
# Depends on result size
# ============================

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Input values
a = int(input())

b = int(input())

c = int(input())

d = int(input())

# Compute and print result
print((a ** b) + (c ** d))