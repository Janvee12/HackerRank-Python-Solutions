# ============================
# PLATFORM:
# HackerRank (Python - Sets / Introduction to Sets)
# ============================

# ============================
# PROBLEM:
# Given an array of integers,
# calculate the average of distinct values only.
#
# Steps:
# - Remove duplicate values
# - Find average of unique elements
#
# Example:
# Input:
# [1, 2, 2, 3, 4]
#
# Unique values:
# [1, 2, 3, 4]
#
# Average:
# (1 + 2 + 3 + 4) / 4 = 2.5
# ============================

# ============================
# APPROACH:
#
# 1. Convert list into set
#    to remove duplicates.
#
# 2. Find:
#    - sum of unique values
#    - count of unique values
#
# 3. Compute average:
#       sum / count
#
# 4. Round result to 3 decimal places.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
# → converting list to set
#
# SPACE COMPLEXITY:
# O(n)
# → storing unique elements
# ============================

def average(array):

    # Remove duplicates
    unique_values = set(array)

    # Count unique elements
    length = len(unique_values)

    # Sum of unique elements
    total = sum(unique_values)

    # Return average rounded to 3 decimals
    return round(total / length, 3)


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().split()))

    result = average(arr)

    print(result)