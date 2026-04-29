# ============================
# PLATFORM:
# HackerRank (Python - Conditional Statements)
# ============================

# ============================
# PROBLEM:
# Given a year, determine whether it is a leap year.
#
# A year is a leap year if:
# 1. It is divisible by 4 AND not divisible by 100
# OR
# 2. It is divisible by 400
#
# Return True if it is a leap year, otherwise False.
# ============================

# ============================
# APPROACH:
# 1. Check if year is divisible by 4 and NOT divisible by 100 → leap year
# 2. Else check if year is divisible by 400 → leap year
# 3. Otherwise → not a leap year
# ============================

# ============================
# TIME COMPLEXITY:
# O(1) → constant time (only few conditions checked)
#
# SPACE COMPLEXITY:
# O(1) → no extra space used
# ============================

def is_leap(year):
    leap = False

    if year % 4 == 0 and year % 100 != 0:
        leap = True
    elif year % 400 == 0:
        leap = True

    return leap


# Input & Output
year = int(input())
print(is_leap(year))