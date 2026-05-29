# ============================
# PLATFORM:
# HackerRank
# (Python - Triangle Quest)
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
# 22
# 333
# 4444
#
# Constraint:
# Use less than 2 lines of code.
# ============================

# ============================
# APPROACH:
#
# Mathematical Trick:
#
# ((10^i) // 9)
#
# generates:
#
# 1
# 11
# 111
# 1111
#
# Multiplying by i gives:
#
# 1
# 22
# 333
# 4444
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

# Enter your code here. Read input from STDIN. Print output to STDOUT

for i in range(1, int(input())):

    print(((10 ** i) // 9) * i)