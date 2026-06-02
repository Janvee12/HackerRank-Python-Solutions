# ============================
# PLATFORM:
# HackerRank
# (Python - Built-ins - Athlete Sort)
# ============================

# ============================
# PROBLEM:
#
# You are given:
#
# n = number of athletes
# m = number of attributes
#
# Each athlete has m integers.
#
# You are also given an
# integer k.
#
# Task:
#
# Sort the athletes based on
# the k-th attribute and print
# the sorted table.
#
# ============================

# ============================
# APPROACH:
#
# Python's sorted() function
# supports a key parameter.
#
# key=lambda x: x[k]
#
# For each row:
#
# x = athlete record
#
# x[k] = value of the
# k-th attribute
#
# sorted() sorts all rows
# according to that value.
#
# ============================

# ============================
# EXAMPLE:
#
# Input:
#
# 5 3
# 10 2 5
# 7 1 0
# 9 9 9
# 1 23 12
# 6 5 9
# 1
#
# k = 1
#
# Sort using column 1:
#
# 2
# 1
# 9
# 23
# 5
#
# Output:
#
# 7 1 0
# 10 2 5
# 6 5 9
# 9 9 9
# 1 23 12
#
# ============================

# ============================
# TIME COMPLEXITY:
#
# Sorting:
# O(n log n)
#
# ============================
#
# SPACE COMPLEXITY:
#
# O(n)
#
# ============================

#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    arr = []

    # Read athlete data
    for _ in range(n):
        arr.append(
            list(map(int, input().rstrip().split()))
        )

    # Column index to sort by
    k = int(input().strip())

    # Sort according to k-th column
    for row in sorted(arr, key=lambda x: x[k]):
        print(*row)