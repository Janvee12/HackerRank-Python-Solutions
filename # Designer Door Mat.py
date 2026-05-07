# ============================
# PLATFORM:
# HackerRank (Python - Strings / Text Alignment)
# ============================

# ============================
# PROBLEM (Designer Door Mat):
# Print a door mat pattern with:
#
# - Pattern: ".|."
# - Center text: "WELCOME"
# - Remaining spaces filled with '-'
#
# Conditions:
# - Number of rows (n) must be odd
# - Number of columns (m) = 3 * n
#
# Example:
# Input:
# 7 21
#
# Output:
# ---------.|.---------
# ------.|..|..|.------
# ---.|..|..|..|..|.---
# -------WELCOME-------
# ---.|..|..|..|..|.---
# ------.|..|..|.------
# ---------.|.---------
# ============================

# ============================
# APPROACH:
#
# 1. Use pattern ".|."
#
# 2. Top Half:
#    - Increase pattern count:
#      1, 3, 5, ...
#
# 3. Middle:
#    - Print "WELCOME" centered
#
# 4. Bottom Half:
#    - Reverse the top half pattern
#
# 5. Use center(width, '-') for alignment
# ============================

# ============================
# TIME COMPLEXITY:
# O(n * m)
# → printing the pattern
#
# SPACE COMPLEXITY:
# O(1)
# ============================

# Read input
n, m = map(int, input().split())

# Pattern string
c = '.|.'

# Middle message
msg = 'WELCOME'

# ============================
# Top Half
# ============================
for i in range(1, n // 2 + 1):
    print((c * (2 * i - 1)).center(m, '-'))

# ============================
# Middle Line
# ============================
print(msg.center(m, '-'))

# ============================
# Bottom Half
# ============================
for i in range(n // 2, 0, -1):
    print((c * (2 * i - 1)).center(m, '-'))