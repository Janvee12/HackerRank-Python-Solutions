# ============================
# PLATFORM:
# HackerRank (Python - Math / Polar Coordinates)
# ============================

# ============================
# PROBLEM:
# You are given a complex number z.
#
# Print:
# 1. The modulus (absolute value)
# 2. The phase angle
#
# Example:
# Input:
# 1+2j
#
# Output:
# 2.23606797749979
# 1.1071487177940904
# ============================

# ============================
# APPROACH:
#
# 1. Read complex number using:
#       complex(input())
#
# 2. Use:
#       abs(z)
#    to find modulus.
#
# 3. Use:
#       phase(z)
#    from cmath module
#    to find phase angle.
#
# ============================

# ============================
# FORMULAS:
#
# For complex number:
#     z = a + bj
#
# Modulus:
#     |z| = √(a² + b²)
#
# Phase:
#     θ = tan⁻¹(b / a)
# ============================

# ============================
# TIME COMPLEXITY:
# O(1)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

from cmath import phase

# Read complex number
inp = complex(input())

# Print modulus
print(abs(inp))

# Print phase angle
print(phase(inp))