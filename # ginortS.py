# ============================
# PLATFORM:
# HackerRank
# (Python - Built-ins - ginortS)
# ============================

# ============================
# PROBLEM:
#
# Sort the string such that:
#
# 1. Lowercase letters
# 2. Uppercase letters
# 3. Odd digits
# 4. Even digits
#
# Each group should be
# sorted individually.
#
# ============================

# ============================
# APPROACH:
#
# Use sorted() with a custom
# key function.
#
# Priority:
#
# Lowercase -> 0
# Uppercase -> 1
# Odd Digit -> 2
# Even Digit -> 3
#
# Then sort lexicographically
# within each category.
#
# ============================

# ============================
# TIME COMPLEXITY:
#
# O(n log n)
#
# ============================
#
# SPACE COMPLEXITY:
#
# O(n)
#
# ============================

# Enter your code here. Read input from STDIN. Print output to STDOUT

user_input = input().strip()

sorted_string = ''.join(
    sorted(
        user_input,
        key=lambda x: (
            x.isdigit() and int(x) % 2 == 0,  # Even digits last
            x.isdigit() and int(x) % 2 != 0,  # Odd digits before even
            x.isupper(),                      # Uppercase after lowercase
            x                                # Sort within category
        )
    )
)

print(sorted_string)