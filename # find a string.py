# ============================
# PLATFORM:
# HackerRank (Python - Strings)
# ============================

# ============================
# PROBLEM (Find a String):
# Given a string and a substring,
# count how many times the substring appears in the string.
#
# NOTE:
# - Overlapping occurrences are allowed.
#
# Example:
# Input:
# string = "ABCDCDC"
# sub_string = "CDC"
#
# Output:
# 2
# ============================

# ============================
# APPROACH:
# 1. Find length of substring and main string.
# 2. Loop through string:
#    - Take substring of length sub_string
#    - Compare with sub_string
# 3. If match → increase count
# 4. Return total count
#
# Important:
# Loop runs till (str_l - sub_l + 1)
# to avoid index out of range
# ============================

# ============================
# TIME COMPLEXITY:
# O(n * m)
# → n = length of string
# → m = length of substring
#
# SPACE COMPLEXITY:
# O(1)
# ============================

def count_substring(string, sub_string):

    sub_l = len(sub_string)
    str_l = len(string)

    count = 0

    for i in range(str_l + 1 - sub_l):

        # Check substring match
        if string[i:i + sub_l] == sub_string:
            count += 1

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)