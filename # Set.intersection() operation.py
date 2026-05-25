# ============================
# PLATFORM:
# HackerRank
# (Python - Sets / Set .intersection() Operation)
# ============================

# ============================
# PROBLEM:
# You are given two sets
# of student roll numbers:
#
# - English newspaper subscribers
# - French newspaper subscribers
#
# Task:
# Find the total number
# of students who subscribed
# to BOTH newspapers.
#
# Example:
#
# English:
# {1, 2, 3}
#
# French:
# {2, 3, 4}
#
# Intersection:
# {2, 3}
#
# Output:
# 2
# ============================

# ============================
# APPROACH:
#
# Use SET INTERSECTION
#
# intersection():
# returns common elements
# present in both sets.
#
# Steps:
#
# 1. Read English roll numbers.
#
# 2. Read French roll numbers.
#
# 3. Find common students using:
#
#       rolle.intersection(rollf)
#
# 4. Print length of result.
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
n = int(input())

# English roll numbers
rolle = set(input().split())

# Number of French subscribers
f = int(input())

# French roll numbers
rollf = set(input().split())

# Count common students
output = len(rolle.intersection(rollf))

# Print answer
print(output)