# ============================
# PLATFORM:
# HackerRank
# (Python - Built-ins - Python Evaluation)
# ============================

# ============================
# PROBLEM:
#
# You are given a string
# containing a valid Python
# expression or statement.
#
# Task:
#
# Evaluate the expression
# using Python's built-in
# eval() function.
#
# ============================

# ============================
# APPROACH:
#
# 1. Read the input string.
#
# 2. Use eval() to execute
#    the expression.
#
# 3. No extra print statement
#    is required because the
#    input itself may contain
#    a print() function.
#
# Example:
#
# Input:
#
# print(2 + 3)
#
# eval() executes:
#
# print(2 + 3)
#
# Output:
#
# 5
#
# ============================

# ============================
# TIME COMPLEXITY:
#
# O(n)
#
# n = length of input string
#
# ============================

# ============================
# SPACE COMPLEXITY:
#
# O(1)
#
# (excluding input storage)
#
# ============================

# Enter your code here.
# Read input from STDIN.
# Print output to STDOUT

expression = input().strip()

eval(expression)