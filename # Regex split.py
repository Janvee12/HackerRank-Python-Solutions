# ============================
# PLATFORM:
# HackerRank
# (Python - Regex Split)
# ============================

# ============================
# PROBLEM:
# ============================
#
# You are given a string.
# You need to split it using
# the delimiters:
#
#   ,  (comma)
#   .  (dot)
#
# Print each part on a new line.
#
# ============================
# APPROACH:
# ============================
#
# Use Python regex split:
#
# re.split(pattern, string)
#
# Pattern:
#   [,.]
#
# This means:
#   split on comma OR dot
#
# ============================

import re

# regex pattern:
# [,.] → matches either ',' or '.'
regex_pattern = r"[,.]"

# read input string
text = input()

# split string by commas and dots
parts = re.split(regex_pattern, text)

# print each part on new line
print("\n".join(parts))