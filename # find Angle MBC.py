# ============================
# PLATFORM:
# HackerRank (Python - Math / Find Angle MBC)
# ============================

# ============================
# PROBLEM:
# Given:
# - AB = perpendicular side
# - BC = base side
#
# Triangle ABC is right-angled at B.
#
# Task:
# Find angle MBC in degrees
# and print it with the degree symbol.
#
# Example:
# Input:
# 10
# 10
#
# Output:
# 45°
# ============================

# ============================
# APPROACH:
#
# Using Trigonometry:
#
# tan(θ) = opposite / adjacent
#
# Here:
# opposite = AB
# adjacent = BC
#
# So:
#
# θ = atan(AB / BC)
#
# Steps:
#
# 1. Use math.atan()
#    to calculate angle in radians.
#
# 2. Convert radians to degrees
#    using math.degrees().
#
# 3. Round the result.
#
# 4. Print with degree symbol.
#
# ============================

# ============================
# FORMULA:
#
# θ = tan⁻¹(AB / BC)
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(1)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

import math

# Read sides
AB = int(input())
BC = int(input())

# Calculate angle in radians
theta = math.atan(AB / BC)

# Convert to degrees
theta_degree = round(math.degrees(theta))

# Print with degree symbol
print(theta_degree, chr(176), sep='')