# ============================
# PLATFORM:
# HackerRank
# (Validating Phone Numbers)
# ============================

# ============================
# PROBLEM:
# ============================
#
# Given N phone numbers,
# determine whether each phone
# number is valid or not.
#
# Valid phone number:
#
# ✔ Contains exactly 10 digits
# ✔ Starts with 7, 8, or 9
#
# Print:
# YES -> Valid
# NO  -> Invalid
#
# ============================
# APPROACH:
# ============================
#
# Use Regular Expression:
#
# ^[789]\d{9}$
#
# Explanation:
#
# ^      -> Start of string
# [789]  -> First digit must be 7,8,or 9
# \d{9}  -> Exactly 9 more digits
# $      -> End of string
#
# Total digits = 10
#
# ============================

import re

n = int(input())

for _ in range(n):

    number = input().strip()

    if re.match(r'^[789]\d{9}$', number):
        print("YES")
    else:
        print("NO")
