# ============================
# PLATFORM:
# HackerRank
# (Hex Color Code)
# ============================

# ============================
# PROBLEM:
# ============================
#
# Given CSS code, extract all
# valid hexadecimal color codes.
#
# Valid color codes:
#
#   #FFF
#   #ffffff
#   #A1B2C3
#
# Invalid:
#
#   #12
#   #ABCDE
#   #1234567
#
# Also:
# Ignore lines that start with '#'
# because they are CSS selectors.
#
# ============================
# APPROACH:
# ============================
#
# 1. Read each line.
# 2. Skip lines beginning with '#'.
# 3. Use regex to find:
#
#    #RGB
#    #RRGGBB
#
# 4. Print every match.
#
# ============================

import re

N = int(input())

for _ in range(N):

    line = input()

    # Ignore CSS selectors
    if not re.search(r"^#", line):

        colors = re.findall(
            r"#[A-Fa-f0-9]{6}|#[A-Fa-f0-9]{3}",
            line
        )

        if colors:
            print(*colors, sep="\n")