# ============================
# PLATFORM:
# HackerRank
# (Python - Sets / Symmetric Difference Operation)
# ============================

# ============================
# PROBLEM:
# You are given two sets:
#
# - English newspaper subscribers
# - French newspaper subscribers
#
# Task:
# Find the number of students
# who subscribed to ONLY ONE
# newspaper.
#
# This is called:
#
# SYMMETRIC DIFFERENCE
#
# Example:
#
# English:
# {1, 2, 3}
#
# French:
# {2, 3, 4}
#
# Symmetric Difference:
# {1, 4}
#
# Output:
# 2
# ============================

# ============================
# APPROACH:
#
# Use:
#
# symmetric_difference()
#
# It returns elements present
# in either set
# but NOT in both.
#
# Formula:
#
# (A - B) U (B - A)
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n + m)
#
# SPACE COMPLEXITY:
# O(n + m)
# ============================

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Number of English subscribers
n_english = int(input())

# English set
sub_english = set(
    map(int, input().split())
)

# Number of French subscribers
n_french = int(input())

# French set
sub_french = set(
    map(int, input().split())
)

# Symmetric difference
result = sub_english.symmetric_difference(
    sub_french
)

# Print answer
print(len(result))