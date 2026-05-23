# ============================
# PLATFORM:
# HackerRank
# (Python - Sets / Set Union Operation)
# ============================

# ============================
# PROBLEM:
# You are given two sets
# containing roll numbers
# of students subscribed
# to English and French newspapers.
#
# Task:
# Find the total number
# of students who subscribed
# to at least one newspaper.
#
# Example:
#
# English:
# {1, 2, 3}
#
# French:
# {2, 3, 4}
#
# Union:
# {1, 2, 3, 4}
#
# Output:
# 4
# ============================

# ============================
# APPROACH:
#
# Use SET UNION
#
# union():
# combines all unique elements
# from both sets.
#
# Steps:
#
# 1. Read English roll numbers.
#
# 2. Read French roll numbers.
#
# 3. Find:
#
#       rolle.union(rollf)
#
# 4. Print length of union set.
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
rolle = set(map(int, input().split()))

# Number of French subscribers
f = int(input())

# French roll numbers
rollf = set(map(int, input().split()))

# Total unique students
output = len(rolle.union(rollf))

# Print answer
print(output)