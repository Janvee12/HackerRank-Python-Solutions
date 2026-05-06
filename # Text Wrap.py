# ============================
# PLATFORM:
# HackerRank (Python - Strings / Text Wrap)
# ============================

# ============================
# PROBLEM (Text Wrap):
# Given a string and a maximum width,
# break the string into multiple lines such that
# each line has at most max_width characters.
#
# Print the wrapped string line by line.
#
# Example:
# Input:
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
#
# Output:
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ
# ============================

# ============================
# APPROACH:
# 1. Use textwrap.wrap() function.
#    - It splits the string into chunks of size max_width.
# 2. Join the list using '\n' to print each chunk on new line.
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
# → traverse string once
#
# SPACE COMPLEXITY:
# O(n)
# → store wrapped list
# ============================

import textwrap

def wrap(string, max_width):
    stringlist = textwrap.wrap(string, max_width)
    return "\n".join(stringlist)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)