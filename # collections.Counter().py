# ============================
# PLATFORM:
# HackerRank (Python - Collections / collections.Counter())
# ============================

# ============================
# PROBLEM:
# A shoe shop has:
# - X shoes
# - each shoe has a size
#
# Customers want specific shoe sizes
# and offer a price.
#
# Rules:
# - If requested size is available:
#       sell shoe
#       add price to total money
#       reduce stock count
#
# - Otherwise:
#       ignore customer
#
# Task:
# Print total money earned.
#
# Example:
# Input:
# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50
#
# Output:
# 200
# ============================

# ============================
# APPROACH:
#
# 1. Use Counter to store frequency
#    of each shoe size.
#
# Example:
# sizes = [2,2,3]
#
# Counter:
# {
#   2:2,
#   3:1
# }
#
# 2. For each customer:
#    - check if size available
#    - if yes:
#         add price
#         decrease count
#
# 3. Print total earned money.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(n + m)
#
# n = number of shoes
# m = number of customers
#
# SPACE COMPLEXITY:
# O(n)
# → Counter storage
# ============================

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

# Number of shoes
X = int(input())

# Shoe sizes list
sizes = [int(i) for i in input().split()]

# Number of customers
N = int(input())

# Count frequency of each size
sizes = Counter(sizes)

# Total money earned
money = 0

# Process customers
for i in range(N):

    size, price = [int(j) for j in input().split()]

    # If shoe available
    if size in sizes and sizes[size] > 0:

        money += price

        # Reduce stock
        sizes[size] -= 1

# Print total earnings
print(money)