# ============================
# PLATFORM:
# HackerRank (Python - Strings / Alphabet Rangoli)
# ============================

# ============================
# PROBLEM (Alphabet Rangoli):
# Print an alphabet rangoli pattern of size n.
#
# Rules:
# - Use lowercase English letters
# - Letters should form a symmetric pattern
# - Use '-' between letters
# - Pattern must be centered
#
# Example:
# Input:
# 3
#
# Output:
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----
# ============================

# ============================
# APPROACH:
#
# 1. Build upper half:
#    - Start from largest character
#    - Move toward smaller characters
#
# 2. Create symmetric row:
#    left part + reversed(right part)
#
# 3. Join letters using '-'
#
# 4. Use center() for alignment
#
# 5. Repeat in reverse order for bottom half
# ============================

# ============================
# TIME COMPLEXITY:
# O(n^2)
# → building each row
#
# SPACE COMPLEXITY:
# O(n)
# → temporary row storage
# ============================

def print_rangoli(size):

    # ============================
    # Upper Half
    # ============================
    for i in range(size):

        s = []

        # Descending characters
        s.extend([
            chr(c)
            for c in range(96 + size, 96 + size - i - 1, -1)
        ])

        # Ascending characters
        s.extend([
            chr(c)
            for c in range(96 + size, 96 + size - i, -1)
        ][::-1])

        # Print centered row
        print("-".join(s).center(4 * size - 3, '-'))

    # ============================
    # Lower Half
    # ============================
    for i in range(size - 2, -1, -1):

        s = []

        # Descending characters
        s.extend([
            chr(c)
            for c in range(96 + size, 96 + size - i - 1, -1)
        ])

        # Ascending characters
        s.extend([
            chr(c)
            for c in range(96 + size, 96 + size - i, -1)
        ][::-1])

        # Print centered row
        print("-".join(s).center(4 * size - 3, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)