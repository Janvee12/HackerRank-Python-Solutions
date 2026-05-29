# ============================
# PLATFORM:
# HackerRank
# (Python - Collections / The Captain's Room)
# ============================

# ============================
# PROBLEM:
# A group of tourists
# stays in hotel rooms.
#
# - Every family room number
#   appears exactly K times.
#
# - Captain's room number
#   appears only once.
#
# Task:
# Find the Captain's room number.
#
# Example:
#
# Input:
# 5
# 1 2 3 6 6 6 1 1 1 2 2 2 3 3 3
#
# Output:
# 6
# ============================

# ============================
# APPROACH:
#
# Use Counter
#
# Counter stores:
#
# room_number -> frequency
#
# Captain's room
# has frequency 1.
#
# Traverse dictionary
# and print the key
# whose count is 1.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
#
# SPACE COMPLEXITY:
# O(n)
# ============================

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

# Group size
K = int(input())

# Room numbers
N = input().split()

# Count frequencies
dic = Counter(N)

# Find room appearing once
for i in dic:

    if dic[i] == 1:

        print(i)