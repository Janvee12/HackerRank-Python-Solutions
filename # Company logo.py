# ============================
# PLATFORM:
# HackerRank
# (Python - Collections / Company Logo)
# ============================

# ============================
# PROBLEM:
# Given a string s,
# print the 3 most common characters
# along with their frequencies.
#
# Rules:
#
# 1. Sort by highest frequency.
#
# 2. If frequencies are same,
#    sort alphabetically.
#
# Example:
#
# Input:
# aabbbccde
#
# Output:
# b 3
# a 2
# c 2
# ============================

# ============================
# APPROACH:
#
# Use collections.Counter
#
# Steps:
#
# 1. Sort string alphabetically.
#
#    Why?
#    Because Counter.most_common()
#    preserves first occurrence order
#    for equal frequencies.
#
# 2. Count frequencies using Counter.
#
# 3. Get top 3 characters
#    using:
#
#       most_common(3)
#
# 4. Print character and frequency.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n log n)
#
# Sorting dominates.
#
# SPACE COMPLEXITY:
# O(n)
# ============================

#!/bin/python3

from collections import Counter

import math
import os
import random
import re
import sys

if __name__ == '__main__':

    # Input string
    s = input()

    # Sort string and count frequency
    result = Counter(sorted(s)).most_common(3)

    # Print top 3 characters
    for key, value in result:

        print(key, value)