# ============================
# PLATFORM:
# LeetCode Biweekly Contest
# PROBLEM:
# Zig-Zag Arrays
# ============================

# ============================
# PROBLEM:
# ============================
#
# Count the number of arrays of
# length n.
#
# Each element lies in:
#
#     l ≤ arr[i] ≤ r
#
# The array must follow a
# zig-zag pattern:
#
# arr[0] < arr[1] > arr[2] < arr[3] ...
#
# OR
#
# arr[0] > arr[1] < arr[2] > arr[3] ...
#
# Return the answer modulo:
#
#     10^9 + 7
#
# ============================

# ============================
# APPROACH:
# Dynamic Programming
# Prefix/Suffix Sum Optimization
# ============================

MOD = 10**9 + 7

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:

        MOD = 10**9 + 7

        # Compress values to 0...(r-l)
        r -= l

        # dp[i][j]
        # Number of ways to build
        # first i+1 elements where
        # current value = j

        dp = [[0] * (r + 1) for _ in range(n)]

        # First position can be any value
        for j in range(r + 1):
            dp[0][j] = 1

        for i in range(1, n):

            prev = 0

            # Odd index:
            # arr[i-1] < arr[i]
            if i % 2 == 1:

                for j in range(r + 1):
                    dp[i][j] = prev
                    prev = (prev + dp[i - 1][j]) % MOD

            # Even index:
            # arr[i-1] > arr[i]
            else:

                for j in range(r, -1, -1):
                    dp[i][j] = prev
                    prev = (prev + dp[i - 1][j]) % MOD

        return (sum(dp[-1]) * 2) % MOD