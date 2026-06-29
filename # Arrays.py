# ============================
# PLATFORM:
# HackerRank
# PROBLEM:
# Arrays (NumPy)
# ============================

import numpy

def arrays(arr):
    # Convert list elements to float
    arr = numpy.array(arr, float)

    # Reverse the array
    return arr[::-1]


arr = input().strip().split(' ')
result = arrays(arr)
print(result)