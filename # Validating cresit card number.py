# ============================
# PLATFORM:
# HackerRank
# PROBLEM:
# Validating Credit Card Numbers
# ============================

# ============================
# PROBLEM:
# ============================
#
# A valid credit card number:
#
# 1. Must start with:
#       4, 5, or 6
#
# 2. Must contain exactly
#    16 digits.
#
# 3. Digits may be grouped
#    into four groups of four
#    digits separated by '-'.
#
#    Valid:
#    4123456789123456
#    4123-4567-8912-3456
#
# 4. No other separators are
#    allowed.
#
# 5. Must not contain four or
#    more consecutive repeated
#    digits.
#
# ============================

# ============================
# APPROACH:
# ============================
#
# Step 1:
# Check the card format.
#
# Step 2:
# Remove hyphens.
#
# Step 3:
# Check whether any digit
# appears 4 consecutive times.
#
# ============================

import re

for _ in range(int(input())):

    card = input().strip()

    # Valid formats:
    # 4123456789123456
    # 4123-4567-8912-3456
    pattern = r'^[456]\d{15}$|^[456]\d{3}(-\d{4}){3}$'

    if re.fullmatch(pattern, card):

        # Remove hyphens
        digits = card.replace('-', '')

        # Four consecutive repeated digits
        if re.search(r'(\d)\1{3}', digits):
            print("Invalid")
        else:
            print("Valid")

    else:
        print("Invalid")