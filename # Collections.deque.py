# ============================
# PLATFORM:
# HackerRank
# (Python - Collections / collections.deque())
# ============================

# ============================
# PROBLEM:
# You are given multiple operations
# to perform on a deque.
#
# Operations:
#
# - append x
# - appendleft x
# - pop
# - popleft
#
# Task:
# Perform all operations
# and print final deque elements.
#
# Example:
#
# Input:
# 6
# append 1
# append 2
# appendleft 3
# pop
# popleft
# append 4
#
# Output:
# 1 4
# ============================

# ============================
# APPROACH:
#
# 1. Use collections.deque
#
# 2. Process each command:
#
#    - append(x)
#    - appendleft(x)
#    - pop()
#    - popleft()
#
# 3. Print final deque.
#
# ============================

# ============================
# WHY DEQUE?
#
# deque supports:
#
# - O(1) append/pop from both ends
#
# unlike list which is slower
# for left-side operations.
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
#
# SPACE COMPLEXITY:
# O(n)
# ============================

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

# Number of operations
a = int(input())

# Create deque
d = deque()

# Process operations
for i in range(a):

    b = input().split()

    # Append at right
    if b[0] == 'append':

        d.append(b[1])

    # Append at left
    elif b[0] == 'appendleft':

        d.appendleft(b[1])

    # Remove from right
    elif b[0] == 'pop':

        d.pop()

    # Remove from left
    elif b[0] == 'popleft':

        d.popleft()

# Print deque elements
for i in d:

    print(int(i), end=" ")