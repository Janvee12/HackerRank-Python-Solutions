# ============================
# PLATFORM:
# HackerRank
# (Validating and Parsing Email Addresses)
# ============================

# ============================
# PROBLEM:
# ============================
#
# You are given N lines containing:
#
#     Name <email_address>
#
# Print only those entries whose
# email address is valid.
#
# ============================
# VALID EMAIL RULES:
# ============================
#
# Username:
# ✔ Starts with a letter
# ✔ Can contain:
#     letters
#     digits
#     -
#     _
#     .
#
# Website:
# ✔ Letters only
#
# Extension:
# ✔ Letters only
# ✔ Length between 1 and 3
#
# ============================

import re
import email.utils

for _ in range(int(input())):

    # Parse name and email
    parsed = email.utils.parseaddr(input())

    # ============================
    # REGEX PATTERN
    # ============================
    pattern = r'^[a-zA-Z][\w.\-_]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'

    # Validate email part
    if re.fullmatch(pattern, parsed[-1]):

        # Print in standard format
        print(email.utils.formataddr(parsed))