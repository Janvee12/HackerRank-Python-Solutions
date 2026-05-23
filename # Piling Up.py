# ============================
# PLATFORM:
# HackerRank
# (Python - Collections / Piling Up!)
# ============================

# ============================
# PROBLEM:
# You are given cubes
# with different side lengths
# arranged in a deque.
#
# You may pick cubes only
# from:
#
# - left end
# - right end
#
# Task:
# Determine if cubes can be piled
# such that every next cube
# is smaller than or equal
# to the previous cube.
#
# Output:
# "Yes" or "No"
#
# Example:
#
# Input:
# 1
# 6
# 4 3 2 1 3 4
#
# Output:
# Yes
# ============================

# ============================
# APPROACH:
#
# Greedy Strategy
#
# Always pick the larger cube
# from the two ends.
#
# Why?
#
# To maintain decreasing order.
#
# Steps:
#
# 1. Compare left and right cube.
#
# 2. Remove larger one.
#
# 3. Ensure remaining cubes
#    are not larger than
#    the chosen cube.
#
# 4. If condition breaks:
#       return "No"
#
# 5. If all cubes processed:
#       return "Yes"
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
#
# SPACE COMPLEXITY:
# O(n)
# ============================

from collections import deque

def piling(d):

    while d:

        large = None

        # Choose larger cube
        if d[-1] > d[0]:

            large = d.pop()

        else:

            large = d.popleft()

        # Last cube placed successfully
        if len(d) == 0:

            return "Yes"

        # Invalid piling condition
        if d[-1] > large or d[0] > large:

            return "No"

# Test cases
for i in range(int(input())):

    no_of_cubes = int(input())

    d = deque(map(int, input().split()))

    print(piling(d))