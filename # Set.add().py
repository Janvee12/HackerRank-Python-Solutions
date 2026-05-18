# ============================
# PLATFORM:
# HackerRank (Python - Sets / Set .add())
# ============================

# ============================
# PROBLEM:
# You are given n country names.
#
# Task:
# Print the number of distinct
# country names.
#
# Example:
#
# Input:
# 7
# UK
# China
# USA
# France
# New Zealand
# UK
# France
#
# Output:
# 5
# ============================

# ============================
# APPROACH:
#
# 1. Create an empty set.
#
# 2. Read each country name.
#
# 3. Add country to set.
#
# 4. Since sets store only unique values,
#    duplicates are automatically removed.
#
# 5. Print size of set.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
#
# SPACE COMPLEXITY:
# O(n)
# → storing unique countries
# ============================

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Create empty set
s = set()

# Number of country names
n = int(input())

# Read country names
for i in range(n):

    country = input()

    s.add(country)

# Print count of unique countries
print(len(s))