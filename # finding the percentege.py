# ============================
# PLATFORM:
# HackerRank (Python - Dictionaries)
# ============================

# ============================
# PROBLEM (Finding the Percentage):
# You are given n students' names and their marks.
#
# Store the data in a dictionary where:
#   key = student name
#   value = list of scores
#
# Then you are given a student's name (query_name).
#
# Task:
# Print the average marks of that student,
# formatted to 2 decimal places.
#
# Example:
# Input:
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
#
# Output:
# 56.00
# ============================

# ============================
# APPROACH:
# 1. Read n (number of students).
# 2. Use dictionary to store:
#       name → list of marks
# 3. Read query_name.
# 4. Retrieve marks of that student.
# 5. Compute average = sum(scores) / len(scores)
# 6. Print result with 2 decimal places.
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
# → reading input and computing average
#
# SPACE COMPLEXITY:
# O(n)
# → storing dictionary
# ============================

if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    # Input and dictionary creation
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    # Query student name
    query_name = input()

    # Calculate average
    scores = student_marks[query_name]
    avg = sum(scores) / len(scores)

    # Print formatted output
    print(f"{avg:.2f}")