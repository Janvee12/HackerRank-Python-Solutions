# ============================
# PLATFORM:
# HackerRank (Python - Strings / Capitalize!)
# ============================

# ============================
# PROBLEM (Capitalize!):
# Given a string s,
# capitalize the first character of each word.
#
# Example:
# Input:
# hello world
#
# Output:
# Hello World
#
# NOTE:
# Words are separated by spaces.
# ============================

# ============================
# APPROACH:
#
# 1. Split the string into words using split(" ").
#
# 2. Capitalize each word using:
#       capitalize()
#
# 3. Join the words back using spaces.
#
# 4. Return final string.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
# → Traverse all characters once
#
# SPACE COMPLEXITY:
# O(n)
# → Store split words
# ============================

#!/bin/python3

import math
import os
import random
import re
import sys


# ============================
# FUNCTION
# ============================

def solve(s):

    # Split string into words
    s = s.split(" ")

    # Capitalize each word
    s = [word.capitalize() for word in s]

    # Join words back into string
    s = " ".join(s)

    return s


# ============================
# DRIVER CODE
# ============================

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()