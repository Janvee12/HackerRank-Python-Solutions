# ============================
# PLATFORM:
# HackerRank
# (Python - Sets / Set .difference() Operation)
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
# who subscribed ONLY
# to the English newspaper.
#
# Example:
#
# English:
# {1, 2, 3}
#
# French:
# {2, 3, 4}
#
# Difference:
# {1}
#
# Output:
# 1
# ============================

# ============================
# APPROACH:
#
# Use SET DIFFERENCE
#
# A.difference(B)
#
# returns elements present in A
# but not in B.
#
# Steps:
#
# 1. Read English set.
#
# 2. Read French set.
#
# 3. Compute:
#
#       set(A).difference(set(B))
#
# 4. Print size of result.
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
a = int(input())

# English set
A = input().split()

# Number of French subscribers
b = int(input())

# French set
B = input().split()

# Students subscribed only to English
print(len(set(A).difference(set(B))))