# ============================
# PLATFORM:
# HackerRank (Python - Strings / The Minion Game)
# ============================

# ============================
# PROBLEM (The Minion Game):
#
# Two players:
# - Kevin → creates substrings starting with vowels
# - Stuart → creates substrings starting with consonants
#
# Rules:
# - Score = number of possible substrings
#   starting from each position
#
# Task:
# Print:
# - Winner name
# - Winner score
# OR "Draw"
#
# Example:
# Input:
# BANANA
#
# Output:
# Stuart 12
# ============================

# ============================
# APPROACH:
#
# Key Observation:
#
# Number of substrings starting at index i:
#       n - i
#
# Example:
# BANANA
#
# Index 0:
# BANANA
# ANANA
# NANA
# ANA
# NA
# A
#
# Total = 6 = n - 0
#
# Steps:
#
# 1. Traverse each character.
#
# 2. If character is vowel:
#       Kevin score += (n - i)
#
# 3. Else:
#       Stuart score += (n - i)
#
# 4. Compare scores and print result.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
# → Single traversal
#
# SPACE COMPLEXITY:
# O(1)
# ============================

def minion_game(string):

    vowels = "AEIOU"

    ks = 0   # Kevin score
    ss = 0   # Stuart score

    n = len(string)

    for i in range(n):

        # Vowel → Kevin
        if string[i] in vowels:
            ks += (n - i)

        # Consonant → Stuart
        else:
            ss += (n - i)

    # Print winner
    if ks > ss:
        print(f"Kevin {ks}")

    elif ss > ks:
        print(f"Stuart {ss}")

    else:
        print("Draw")


if __name__ == '__main__':

    s = input()

    minion_game(s)