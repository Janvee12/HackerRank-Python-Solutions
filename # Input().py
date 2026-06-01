# ============================
# PLATFORM:
# HackerRank
# (Python - Built-ins - Input())
# ============================

# ============================
# PROBLEM
# ============================
#
# You are given:
#
# x and k
#
# followed by a polynomial
# expression P(x).
#
# Task:
#
# Check whether:
#
#     P(x) == k
#
# Print:
#
# True
# or
# False
#
# ============================

# ============================
# APPROACH
# ============================
#
# Read:
#
# x k
#
# Read polynomial expression.
#
# Example:
#
# x = 1
# k = 4
#
# P(x):
#
# x**3 + x**2 + x + 1
#
# Using eval():
#
# eval(P)
#
# evaluates the expression
# using the current value
# of x.
#
# Then compare the result
# with k.
#
# ============================

# Enter your code here. Read input from STDIN. Print output to STDOUT

x, k = map(int, input().split())

p = input()

print(eval(p) == k)