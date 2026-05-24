# ============================
# PLATFORM:
# HackerRank
# (Python - Triangle Quest 2)
# ============================

# ============================
# PROBLEM:
# Print the following pattern:
#
# Input:
# 5
#
# Output:
# 1
# 121
# 12321
# 1234321
# 123454321
#
# Constraints:
#
# - Use only arithmetic operations
# - No string manipulation
# - Maximum 2 lines of code
# ============================

# ============================
# APPROACH:
#
# Mathematical Trick:
#
# ((10^i) // 9)
#
# creates:
#
# 1
# 11
# 111
# 1111
#
# Squaring them gives:
#
# 1
# 121
# 12321
# 1234321
#
# which forms the required pattern.
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

for i in range(1, int(input()) + 1):
    print(((10**i) // 9) ** 2)