# ============================
# PLATFORM:
# HackerRank (Python - Collections / Word Order)
# ============================

# ============================
# PROBLEM:
# You are given n words.
#
# Task:
#
# 1. Count the number of distinct words.
#
# 2. Print frequencies of words
#    in the order of their
#    first appearance.
#
# Example:
#
# Input:
# 4
# bcdef
# abcdefg
# bcde
# bcdef
#
# Output:
# 3
# 2 1 1
# ============================

# ============================
# APPROACH:
#
# Use OrderedDict
#
# Why OrderedDict?
#
# It preserves insertion order.
#
# Steps:
#
# 1. Create OrderedDict.
#
# 2. For each word:
#
#    - if not present:
#         initialize frequency = 1
#
#    - otherwise:
#         increment frequency
#
# 3. Print:
#
#    - number of distinct words
#    - all frequencies
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

from collections import OrderedDict

# Ordered dictionary
od = OrderedDict()

# Number of words
for i in range(int(input())):

    word = input()

    # First occurrence
    if word not in od:

        od[word] = 1

    # Increase frequency
    else:

        od[word] += 1

# Print number of distinct words
print(len(od))

# Print frequencies
print(*od.values())