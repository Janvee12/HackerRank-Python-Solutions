# ============================
# PLATFORM:
# HackerRank
# (Python - Built-ins -
# Any or All)
# ============================

# ============================
# PROBLEM:
#
# You are given N integers.
#
# Print True if:
#
# 1. All integers are positive.
#
# AND
#
# 2. At least one integer
#    is a palindrome.
#
# Otherwise print False.
#
# ============================

# ============================
# APPROACH:
#
# all()
#
# Checks whether every
# number is positive.
#
# ----------------------------
#
# any()
#
# Checks whether at least
# one number is a palindrome.
#
# A palindrome remains the
# same after reversing.
#
# Example:
#
# 121 -> 121
#
# str(x) == str(x)[::-1]
#
# ----------------------------
#
# Final Answer:
#
# all(positive)
# AND
# any(palindrome)
#
# ============================

# ============================
# TIME COMPLEXITY:
#
# O(N × D)
#
# N = number of integers
# D = number of digits
#
# ============================
#
# SPACE COMPLEXITY:
#
# O(1)
#
# ============================

# Enter your code here.
# Read input from STDIN.
# Print output to STDOUT

n = int(input())

numbers = list(
    map(int, input().split())
)

print(
    all(x > 0 for x in numbers)
    and
    any(
        str(x) == str(x)[::-1]
        for x in numbers
    )
)