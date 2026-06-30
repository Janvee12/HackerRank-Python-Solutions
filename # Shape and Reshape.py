# ============================
# PLATFORM:
# HackerRank
# PROBLEM:
# Shape and Reshape (NumPy)
# ============================

import numpy as np

# Read 9 integers from input
l = list(map(int, input().split()))

# Convert list into NumPy array
arr = np.array(l)

# Reshape the array into a 3 × 3 matrix
arr.shape = (3, 3)

# Print the reshaped array
print(arr)