# ============================
# PLATFORM:
# HackerRank (Python - Errors and Exceptions)
# ============================

# ============================
# PROBLEM:
# You are given multiple test cases.
#
# For each test case:
# - Read two values a and b
# - Print integer division: a // b
#
# Handle errors:
#
# 1. ZeroDivisionError:
#    when b == 0
#
# 2. ValueError:
#    when inputs are not valid integers
#
# Output appropriate error messages.
#
# ============================

# ============================
# APPROACH:
#
# 1. Run loop for all test cases.
#
# 2. Try:
#    - convert inputs to integers
#    - perform integer division
#
# 3. Catch exceptions:
#
#    a) ZeroDivisionError:
#       print custom message
#
#    b) ValueError:
#       print error message from exception
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(t)
#
# t = number of test cases
#
# SPACE COMPLEXITY:
# O(1)
# ============================

# Enter your code here. Read input from STDIN. Print output to STDOUT

for i in range(int(input())):

    a, b = input().split()

    try:
        print(int(a) // int(b))

    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")

    except ValueError as e:
        print("Error Code:", e)