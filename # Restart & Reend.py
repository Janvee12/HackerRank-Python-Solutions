# ============================
# PLATFORM:
# HackerRank
# (Regex - Find All Overlapping Matches)
# ============================

# ============================
# PROBLEM:
# ============================
#
# You are given:
#   S → main string
#   k → pattern string
#
# Task:
# Find ALL occurrences of k in S,
# including OVERLAPPING matches.
#
# Print each match as:
#   (start_index, end_index)
#
# If no match → print (-1, -1)
#
# ============================
# APPROACH:
# ============================
#
# Normal regex findall does NOT detect overlaps.
#
# So we use:
#
#   (?=(k))
#
# This is a LOOKAHEAD trick.
#
# ============================

import re

# input strings
S = input()
k = input()

# ============================
# STEP 1: Overlapping regex
# ============================
#
# (?=(k))
# → matches position where k starts
# → allows overlapping matches
#
pattern = r'(?=(' + re.escape(k) + '))'

matches = re.finditer(pattern, S)

# ============================
# STEP 2: Print results
# ============================
any_match = False

for match in matches:
    any_match = True

    # match.start(1) → start of matched substring
    # match.end(1) - 1 → last index of substring
    print((match.start(1), match.end(1) - 1))

# ============================
# STEP 3: No match case
# ============================
if not any_match:
    print((-1, -1))