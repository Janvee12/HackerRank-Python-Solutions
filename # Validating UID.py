# ============================
# PLATFORM:
# HackerRank
# PROBLEM:
# Validating UID
# ============================

# ============================
# PROBLEM:
# ============================
#
# A valid UID must satisfy:
#
# 1. Exactly 10 characters.
# 2. Only alphanumeric characters.
# 3. At least 2 uppercase letters.
# 4. At least 3 digits.
# 5. No repeated characters.
#
# Print:
# Valid
# or
# Invalid
#
# ============================

# ============================
# APPROACH:
# ============================
#
# Use Regular Expressions:
#
# 1. ^[a-zA-Z0-9]{10}$
#    -> Exactly 10 alphanumeric
#       characters.
#
# 2. [A-Z].*[A-Z]
#    -> At least 2 uppercase
#       letters.
#
# 3. \d.*\d.*\d
#    -> At least 3 digits.
#
# 4. ([A-Za-z0-9]).*(?=\1)
#    -> Checks for duplicate
#       characters.
#
# If all conditions are satisfied
# and no duplicates exist,
# print "Valid".
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

import re

for _ in range(int(input())):

    uid = input().strip()

    # Exactly 10 alphanumeric characters
    if not re.search(r'^[A-Za-z0-9]{10}$', uid):
        print("Invalid")
        continue

    # At least 2 uppercase letters
    if not re.search(r'[A-Z].*[A-Z]', uid):
        print("Invalid")
        continue

    # At least 3 digits
    if not re.search(r'\d.*\d.*\d', uid):
        print("Invalid")
        continue

    # No repeated characters
    if re.search(r'([A-Za-z0-9]).*(\1)', uid):
        print("Invalid")
        continue

    print("Valid")