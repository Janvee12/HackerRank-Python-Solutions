# ============================
# PLATFORM:
# HackerRank
# (Python - Math / Mod Divmod)
# ============================

# ============================
# PROBLEM:
# Given two integers:
#
#     a
#     b
#
# Use divmod(a, b)
# and print:
#
# 1. Integer division result
# 2. Modulus result
# 3. Tuple returned by divmod
#
# Example:
#
# Input:
# 177
# 10
#
# Output:
# 17
# 7
# (17, 7)
# ============================

# ============================
# APPROACH:
#
# Python divmod(a, b)
# returns:
#
#     (a // b, a % b)
#
# where:
#
# // -> quotient
# %  -> remainder
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(1)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

# Read input
a = int(input())

b = int(input())

# divmod returns:
# (quotient, remainder)
op = divmod(a, b)

# Print quotient
print(op[0])

# Print remainder
print(op[1])

# Print tuple
print(op)