# ============================
# PLATFORM:
# HackerRank (Python - Strings / Text Alignment)
# ============================

# ============================
# PROBLEM (Text Alignment):
# Print a stylized 'H' logo using alignment methods:
#   rjust(), ljust(), center()
#
# Input:
# thickness (odd number)
#
# Output:
# Properly aligned pattern using character 'H'
# ============================

# ============================
# APPROACH:
#
# Use string alignment functions:
# - rjust(width)  → right align
# - ljust(width)  → left align
# - center(width) → center align
#
# Build the pattern in 5 parts:
# 1. Top Cone
# 2. Top Pillars
# 3. Middle Belt
# 4. Bottom Pillars
# 5. Bottom Cone
# ============================

# ============================
# TIME COMPLEXITY:
# O(n^2)
# → printing pattern
#
# SPACE COMPLEXITY:
# O(1)
# ============================

thickness = int(input())  # Must be odd
c = 'H'

# Top Cone
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) +
          (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) +
          (c * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) +
           c +
           (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))