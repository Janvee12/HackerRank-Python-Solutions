# ============================
# PLATFORM:
# HackerRank (Python - Strings / Merge the Tools!)
# ============================

# ============================
# PROBLEM (Merge the Tools!):
#
# Given:
# - A string
# - An integer k
#
# Divide the string into substrings of length k.
#
# For each substring:
# - Remove duplicate characters
# - Keep only the first occurrence order
#
# Print each processed substring on a new line.
#
# Example:
# Input:
# AABCAAADA
# 3
#
# Substrings:
# AAB
# CAA
# ADA
#
# Output:
# AB
# CA
# AD
# ============================

# ============================
# APPROACH:
#
# 1. Traverse string in steps of k.
#
# 2. Extract substring:
#       t = string[i:i+k]
#
# 3. Use a set to track seen characters.
#
# 4. Print character only if:
#       character not already seen
#
# 5. Preserve original order.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
# → Each character processed once
#
# SPACE COMPLEXITY:
# O(k)
# → Set stores unique characters
# ============================

def merge_the_tools(string, k):

    # Traverse in chunks of size k
    for i in range(0, len(string), k):

        # Current substring
        t = string[i:i + k]

        # Track unique characters
        seen = set()

        for ch in t:

            # Print only first occurrence
            if ch not in seen:
                print(ch, end='')
                seen.add(ch)

        print()


if __name__ == '__main__':

    string, k = input(), int(input())

    merge_the_tools(string, k)