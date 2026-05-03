# ============================
# PLATFORM:
# HackerRank (Python - Strings)
# ============================

# ============================
# PROBLEM (sWAP cASE):
# Given a string s, swap the case of each character.
#
# - Convert lowercase letters → uppercase
# - Convert uppercase letters → lowercase
#
# Example:
# Input: "Hello World"
# Output: "hELLO wORLD"
# ============================

# ============================
# APPROACH:
# 1. Use built-in string method swapcase()
# 2. It automatically converts:
#    - lowercase → uppercase
#    - uppercase → lowercase
# 3. Return the modified string
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
# → Each character is processed once
#
# SPACE COMPLEXITY:
# O(n)
# → New string is created
# ============================

def swap_case(s):
    return s.swapcase()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)