# ============================
# PLATFORM:
# HackerRank (Python - Strings)
# ============================

# ============================
# PROBLEM (Mutations):
# You are given a string.
# You need to change the character at a given index
# to a new character.
#
# Since strings are immutable in Python,
# you cannot modify them directly.
#
# Example:
# Input:
# abracadabra
# 5 k
#
# Output:
# abrackdabra
# ============================

# ============================
# APPROACH:
# 1. Use string slicing:
#    - Take part before index → string[:position]
#    - Add new character
#    - Add remaining part → string[position+1:]
#
# 2. Combine all parts to form new string.
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
# → New string is created
#
# SPACE COMPLEXITY:
# O(n)
# → New string stored
# ============================

def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)