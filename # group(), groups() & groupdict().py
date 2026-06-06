# ============================
# PLATFORM:
# HackerRank
# (String - First Repeated Adjacent Character)
# ============================

# ============================
# PROBLEM:
# ============================
#
# Given a string s,
# find the FIRST character
# that appears twice consecutively.
#
# Example:
#   "abcaab"
# → no adjacent repetition → -1
#
#   "abccde"
# → first repeated adjacent = 'c'
#
# ============================
# APPROACH:
# ============================
#
# We scan the string from left to right.
#
# At each index i:
#   compare s[i] and s[i+1]
#
# If both are same → print and stop.
#
# If no such pair exists → print -1
#
# ============================

s = input().strip()

# loop till second last character
for i in range(len(s) - 1):

    # check adjacent characters
    if s[i] == s[i + 1]:

        print(s[i])
        break

else:
    # executed if loop never breaks
    print(-1)