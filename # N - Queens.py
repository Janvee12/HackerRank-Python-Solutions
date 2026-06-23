# ============================
# PLATFORM:
# LeetCode
# PROBLEM:
# 51. N-Queens
# ============================

# ============================
# PROBLEM:
# ============================
#
# Place n queens on an n × n
# chessboard such that:
#
# 1. No two queens share the
#    same row.
#
# 2. No two queens share the
#    same column.
#
# 3. No two queens share the
#    same diagonal.
#
# Return all possible board
# configurations.
#
# ============================

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        # Used columns
        col = set()

        # Main diagonal (r + c)
        posDiag = set()

        # Anti-diagonal (r - c)
        negDiag = set()

        res = []

        # Empty board
        board = [["."] * n for _ in range(n)]

        def backtrack(r):

            # All queens placed
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):

                # Position is under attack
                if (c in col or
                    (r + c) in posDiag or
                    (r - c) in negDiag):
                    continue

                # Place queen
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                # Move to next row
                backtrack(r + 1)

                # Backtrack
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtrack(0)

        return res