# ============================
# PLATFORM:
# HackerRank
# (Python - Sets / Set Mutations)
# ============================

# ============================
# PROBLEM:
# You are given a set A
# and several set operations.
#
# Operations can be:
#
# - update()
# - intersection_update()
# - difference_update()
# - symmetric_difference_update()
#
# Task:
# Perform all operations
# and print the sum
# of elements remaining in set A.
# ============================

# ============================
# APPROACH:
#
# Use built-in SET methods.
#
# Operations:
#
# 1. update()
#    Adds elements from another set.
#
# 2. difference_update()
#    Removes common elements.
#
# 3. intersection_update()
#    Keeps only common elements.
#
# 4. symmetric_difference_update()
#    Keeps elements present
#    in exactly one set.
#
# ============================

# ============================
# TIME COMPLEXITY:
#
# Depends on operations,
# approximately:
#
# O(total elements processed)
#
# SPACE COMPLEXITY:
# O(n)
# ============================

# Function to apply operation
def updateit(setA, s, command):

    if command == "update":

        setA.update(s)

    elif command == "difference_update":

        setA.difference_update(s)

    elif command == "intersection_update":

        setA.intersection_update(s)

    else:

        setA.symmetric_difference_update(s)

    return setA


# Size of set A
a = int(input())

# Initial set A
setA = set(map(int, input().split()))

# Number of operations
for i in range(int(input())):

    command, len_of_set = input().split()

    s = set(map(int, input().split()))

    setA = updateit(setA, s, command)

# Print sum of final set
print(sum(setA))