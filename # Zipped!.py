# ============================
# PLATFORM:
# HackerRank
# (Python - Built-ins - Zipped!)
# ============================

# ============================
# PROBLEM
# ============================
#
# There are:
#
# N students
# X subjects
#
# Input contains marks
# subject-wise.
#
# Task:
#
# Print the average marks
# obtained by each student.
#
# ============================

# ============================
# APPROACH
# ============================
#
# Input is provided
# subject-wise:
#
# Example:
#
# 3 2
#
# 90 80 70
# 88 89 90
#
# Marks:
#
# Subject 1:
# [90, 80, 70]
#
# Subject 2:
# [88, 89, 90]
#
# We need student-wise marks:
#
# Student 1:
# (90, 88)
#
# Student 2:
# (80, 89)
#
# Student 3:
# (70, 90)
#
# zip(*marks)
#
# transposes rows into columns.
#
# ============================

# Enter your code here. Read input from STDIN. Print output to STDOUT

n, x = map(int, input().split())

marks = []

# Read marks for each subject
for _ in range(x):

    course = list(
        map(float, input().split())
    )

    marks.append(course)

# Convert subject-wise data
# into student-wise data
for student_marks in zip(*marks):

    average = sum(student_marks) / x

    print(average)