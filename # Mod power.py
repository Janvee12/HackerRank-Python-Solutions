# ============================
# PLATFORM:
# HackerRank
# (Python - Math / Power - Mod Power)
# ============================

# ============================
# PROBLEM:
# Given integers:
#
#     a
#     b
#     m
#
# Print:
#
# 1. a^b
# 2. a^b mod m
#
# Example:
#
# Input:
# 3
# 4
# 5
#
# Output:
# 81
# 1
#
# Explanation:
#
# 3^4 = 81
#
# 81 % 5 = 1
# ============================

# ============================
# APPROACH:
#
# Use Python built-in:
#
# pow(a, b)
#
# → computes a^b
#
# pow(a, b, m)
#
# → computes:
#    (a^b) % m
#
# efficiently using
# modular exponentiation.
#
# ============================

# ============================
# TIME COMPLEXITY:
#
# pow(a, b)
# → O(log b)
#
# pow(a, b, m)
# → O(log b)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Input values
a = int(input())

b = int(input())

m = int(input())

# Print:
# a^b
# and
# (a^b) % m
print(
    pow(a, b),
    pow(a, b, m),
    sep="\n"
)