# ============================
# PLATFORM:
# HackerRank
# PROBLEM:
# Matrix Script
# ============================

#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# Read column-wise
decoded = ""

for col in range(m):
    for row in range(n):
        decoded += matrix[row][col]

# Replace symbols between letters/digits with space
print(
    re.sub(
        r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])',
        ' ',
        decoded
    )
)