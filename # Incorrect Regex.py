# ============================
# PLATFORM:
# HackerRank (Python - Regex / Incorrect Regex)
# ============================

# ============================
# PROBLEM:
# You are given multiple regex patterns.
#
# Task:
# Determine whether each regex pattern
# is valid or invalid.
#
# Print:
# - True  → if regex is valid
# - False → if regex is invalid
#
# Example:
#
# Input:
# 2
# .*\
# .*
#
# Output:
# False
# True
# ============================

# ============================
# APPROACH:
#
# 1. Read number of test cases.
#
# 2. For each regex pattern:
#    - try compiling using:
#
#          re.compile(pattern)
#
# 3. If compilation succeeds:
#       print(True)
#
# 4. If regex error occurs:
#       print(False)
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
#
# n = number of regex patterns
#
# SPACE COMPLEXITY:
# O(1)
# ============================

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

# Number of test cases
t = int(input())

# Process each regex pattern
for i in range(t):

    reg = input()

    try:

        # Try compiling regex
        re.compile(reg)

        print(True)

    except re.error:

        print(False)