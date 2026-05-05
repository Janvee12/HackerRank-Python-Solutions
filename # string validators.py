# ============================
# PLATFORM:
# HackerRank (Python - Strings)
# ============================

# ============================
# PROBLEM (String Validators):
# Given a string s, check the following:
#
# 1. If any character is alphanumeric
# 2. If any character is alphabetical
# 3. If any character is a digit
# 4. If any character is lowercase
# 5. If any character is uppercase
#
# Print True/False for each condition in order.
#
# Example:
# Input: "qA2"
# Output:
# True
# True
# True
# True
# True
# ============================

# ============================
# APPROACH:
# 1. Initialize flags for each condition as False.
# 2. Traverse each character in the string.
# 3. Use built-in string methods:
#    - isalnum()
#    - isalpha()
#    - isdigit()
#    - islower()
#    - isupper()
# 4. If any condition is satisfied, set flag to True.
# 5. Print all results.
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
# → Traverse string once
#
# SPACE COMPLEXITY:
# O(1)
# ============================

if __name__ == '__main__':
    s = input()

    alnum = False   # alphanumeric
    alph = False    # alphabetic
    digi = False    # digit
    lw = False      # lowercase
    up = False      # uppercase

    for c in s:

        if c.isalnum():
            alnum = True

        if c.isalpha():
            alph = True

        if c.isdigit():
            digi = True

        if c.islower():
            lw = True

        if c.isupper():
            up = True

    print(alnum)
    print(alph)
    print(digi)
    print(lw)
    print(up)