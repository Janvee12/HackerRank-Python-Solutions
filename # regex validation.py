# ============================
# PLATFORM:
# HackerRank
# (Python - Regex Validation)
# ============================

# ============================
# PROBLEM:
# ============================
#
# You are given T strings.
#
# For each string, check if it
# is a valid floating point number.
#
# A valid number:
#
# - May start with + or -
# - Must contain exactly one dot '.'
# - Must have digits after dot
# - Must not contain invalid chars
#
# Output True or False for each.
#
# ============================

# ============================
# APPROACH:
# ============================
#
# Use Regular Expression:
#
# Pattern:
#
# ^[+-]?[0-9]*\.[0-9]+$
#
# Explanation:
#
# ^            → start of string
# [+-]?        → optional sign
# [0-9]*       → digits before dot (optional)
# \.           → literal dot
# [0-9]+       → at least one digit after dot
# $            → end of string
#
# ============================

# ============================
# TIME COMPLEXITY:
# ============================
#
# O(T * L)
# T = number of strings
# L = length of each string
#
# ============================

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

t = int(input())

pattern = r"^[+-]?[0-9]*\.[0-9]+$"

for _ in range(t):
    s = input().strip()
    print(bool(re.match(pattern, s)))