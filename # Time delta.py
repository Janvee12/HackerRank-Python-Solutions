# ============================
# PLATFORM:
# HackerRank (Python - Date and Time / Time Delta)
# ============================

# ============================
# PROBLEM:
# You are given two timestamps t1 and t2.
#
# Task:
# Find the absolute difference
# between the two timestamps in seconds.
#
# Example:
#
# Input:
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
#
# Output:
# 25200
#
# ============================

# ============================
# APPROACH:
#
# 1. Use datetime.strptime()
#    to convert string into datetime object.
#
# 2. Format used:
#
# '%a %d %b %Y %H:%M:%S %z'
#
# where:
# %a -> weekday
# %d -> day
# %b -> month
# %Y -> year
# %H -> hour
# %M -> minute
# %S -> second
# %z -> timezone
#
# 3. Subtract both datetime objects.
#
# 4. Use:
#       total_seconds()
#
# 5. Return absolute difference.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(1)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

#!/bin/python3

import math
import os
import random
import re
import sys

from datetime import datetime

# ============================
# Function:
# Calculate time difference
# ============================
def time_delta(t1, t2):

    # Convert strings into datetime objects
    time1 = datetime.strptime(
        t1,
        '%a %d %b %Y %H:%M:%S %z'
    )

    time2 = datetime.strptime(
        t2,
        '%a %d %b %Y %H:%M:%S %z'
    )

    # Return absolute difference in seconds
    return int(
        abs((time1 - time2).total_seconds())
    )


if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        t1 = input()
        t2 = input()

        print(time_delta(t1, t2))