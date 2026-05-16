# ============================
# PLATFORM:
# HackerRank (Python - Collections / Word Order)
# ============================

# ============================
# PROBLEM:
# You are given n words.
#
# Task:
# 1. Count frequency of each distinct word.
# 2. Print:
#    - number of distinct words
#    - frequencies in order of first appearance
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
# 1. Use dictionary to store:
#
#       word -> frequency
#
# 2. Dictionaries preserve insertion order
#    in Python 3.
#
# 3. For every word:
#    - increase count
#
# 4. Print:
#    - total distinct words
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

# Number of words
n = int(input())

# Dictionary for frequency count
data = {}

# Read words
for i in range(n):

    word = input()

    data[word] = data.get(word, 0) + 1

# Print number of distinct words
print(len(data))

# Print frequencies
print(*data.values())