# ============================
# PLATFORM:
# HackerRank (Python - Strings / String Formatting)
# ============================

# ============================
# PROBLEM (String Formatting):
# Given an integer n,
# print numbers from 1 to n in:
#
# 1. Decimal
# 2. Octal
# 3. Hexadecimal (uppercase)
# 4. Binary
#
# All values should be right-aligned
# based on the width of binary representation of n.
#
# Example:
# Input:
# 5
#
# Output:
# 1 1 1 1
# 2 2 2 10
# 3 3 3 11
# 4 4 4 100
# 5 5 5 101
# ============================

# ============================
# APPROACH:
#
# 1. Find width of largest binary number:
#       len(binary(n))
#
# 2. Loop from 1 → n
#
# 3. Convert number into:
#    - Decimal → d
#    - Octal → o
#    - Hexadecimal → X
#    - Binary → b
#
# 4. Use string formatting with right alignment:
#       {:>{l}}
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n log n)
# → conversion operations for each number
#
# SPACE COMPLEXITY:
# O(1)
# ============================

def print_formatted(number):

    # Width based on binary representation
    l = len("{:b}".format(number))

    for i in range(1, number + 1):

        # Decimal
        d = "{:>{l}d}".format(i, l=l)

        # Octal
        o = "{:>{l}o}".format(i, l=l)

        # Hexadecimal (uppercase)
        X = "{:>{l}X}".format(i, l=l)

        # Binary
        b = "{:>{l}b}".format(i, l=l)

        print(d, o, X, b)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)