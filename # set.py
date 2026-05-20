# ============================
# PLATFORM:
# HackerRank
# (Python - Sets / Set .discard(), .remove() & .pop())
# ============================

# ============================
# PROBLEM:
# You are given a set s
# and a number of operations.
#
# Operations can be:
#
# 1. pop()
#    → removes a random element
#
# 2. remove(x)
#    → removes x
#    → raises error if x not found
#
# 3. discard(x)
#    → removes x if present
#    → no error otherwise
#
# Task:
# Perform all operations
# and print the sum
# of remaining elements.
#
# Example:
#
# Input:
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
#
# Output:
# 38
# ============================

# ============================
# APPROACH:
#
# 1. Read initial set.
#
# 2. For each operation:
#
#    - pop()
#    - remove(x)
#    - discard(x)
#
# 3. Use try-except
#    to avoid KeyError.
#
# 4. Print sum of remaining set.
#
# ============================

# ============================
# DIFFERENCE:
#
# remove(x):
#     Error if x absent
#
# discard(x):
#     No error if x absent
#
# pop():
#     Removes arbitrary element
# ============================

# ============================
# TIME COMPLEXITY:
# O(N)
#
# SPACE COMPLEXITY:
# O(n)
# ============================

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Size of set
n = int(input())

# Initial set
s = set(map(int, input().split()))

# Number of operations
N = int(input())

# Process operations
for op in range(N):

    operation = input()

    try:

        # pop operation
        if operation[0] == 'p':

            s.pop()

        # remove operation
        elif operation[0] == 'r':

            s.remove(int(operation.split()[1]))

        # discard operation
        else:

            s.discard(int(operation.split()[1]))

    except KeyError:

        pass

# Print sum of remaining elements
print(sum(s))