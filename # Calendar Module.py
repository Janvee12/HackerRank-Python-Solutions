```python id="calendar_weekday_hr"
# ============================
# PLATFORM:
# HackerRank (Python - Calendar Module / Find Day of the Week)
# ============================

# ============================
# PROBLEM:
# Given a date (month, day, year),
# determine the day of the week.
#
# Output the day name in UPPERCASE.
#
# Example:
# Input:
# 08 05 2015
#
# Output:
# WEDNESDAY
# ============================

# ============================
# APPROACH:
#
# 1. Use Python's built-in calendar module.
#
# 2. calendar.weekday(year, month, day)
#    returns an integer:
#
#    Monday    = 0
#    Tuesday   = 1
#    ...
#    Sunday    = 6
#
# 3. Use calendar.day_name[index]
#    to get day name string.
#
# 4. Convert result to uppercase.
#
# ============================

# ============================
# TIME COMPLEXITY:
# O(1)
#
# SPACE COMPLEXITY:
# O(1)
# ============================

import calendar

# Read input
m, d, y = map(int, input().split())

# Get weekday index
i = calendar.weekday(y, m, d)

# Print day name in uppercase
print(calendar.day_name[i].upper())
```
