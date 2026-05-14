# ============================
# PLATFORM:
# HackerRank (Python - Collections / namedtuple)
# ============================

# ============================
# PROBLEM:
# You are given details of N students.
#
# Each student has multiple fields like:
# ID, NAME, MARKS, CLASS etc.
#
# Task:
# Find the average of MARKS.
#
# Output result rounded to 2 decimal places.
#
# ============================

# ============================
# APPROACH:
#
# 1. Use namedtuple to create a structured record.
#
# 2. Read column names from input.
#
# 3. For each student:
#    - create Student object
#    - extract MARKS field
#
# 4. Compute:
#       average = total_marks / n
#
# 5. Print result with rounding to 2 decimals.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

from collections import namedtuple

# Number of students
n = int(input())

# Column names (e.g. ID NAME MARKS CLASS)
Student = namedtuple('Student', input())

# Sum of marks
total = sum(
    int(Student(*input().split()).MARKS)
    for i in range(n)
)

# Print average marks
print(round(total / n, 2))