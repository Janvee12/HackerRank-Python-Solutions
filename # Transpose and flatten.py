# ============================
# PLATFORM:
# HackerRank
# PROBLEM:
# Transpose and Flatten (NumPy)
# ============================

import numpy as np

# Read dimensions of the matrix
n, m = map(int, input().split())

# Read matrix elements
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

# Convert list to NumPy array
arr = np.array(matrix)

# Print transpose of the array
print(np.transpose(arr))

# Print flattened array
print(arr.flatten())