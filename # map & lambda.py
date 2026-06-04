# ============================
# PLATFORM:
# HackerRank
# (Python - Map & Lambda)
# ============================

# ============================
# PROBLEM:
# ============================
#
# 1. Generate Fibonacci series
#    of length n
#
# 2. Apply cube function to
#    each Fibonacci number
#
# 3. Print result list
#
# ============================

# ============================
# APPROACH:
# ============================
#
# Step 1: Build Fibonacci list
#
# F(0) = 0
# F(1) = 1
#
# F(n) = F(n-1) + F(n-2)
#
# Step 2: Apply cube:
#
# cube(x) = x^3
#
# Use map(cube, fibonacci)
#
# ============================

# ============================
# TIME COMPLEXITY:
# ============================
#
# Fibonacci generation: O(n)
# Mapping cube: O(n)
#
# Total: O(n)
#
# ============================

# ============================
# SPACE COMPLEXITY:
# ============================
#
# O(n) for storing sequence
#
# ============================

cube = lambda x: x ** 3


def fibonacci(n):

    if n == 0:
        return []

    elif n == 1:
        return [0]

    fib_sequence = [0, 1]

    for i in range(2, n):
        fib_sequence.append(
            fib_sequence[-2] + fib_sequence[-1]
        )

    return fib_sequence


if __name__ == '__main__':

    n = int(input())

    result = list(
        map(cube, fibonacci(n))
    )

    print(result)