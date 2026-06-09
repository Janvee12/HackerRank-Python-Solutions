# ============================
# PLATFORM:
# HackerRank
# (Regex - Roman Numeral Validation)
# ============================

# ============================
# PROBLEM:
# ============================
#
# You are given a string.
# You need to check if it is a VALID ROMAN NUMERAL.
#
# Valid Roman numerals follow rules:
#
# - I, V, X, L, C, D, M
# - No invalid repetition
# - Proper subtractive notation (IV, IX, etc.)
#
# ============================
# APPROACH:
# ============================
#
# We use a FULL REGEX pattern that enforces:
#
# ✔ correct order (M → C → X → I)
# ✔ correct repetition limits
# ✔ correct subtractive combinations
#
# ============================

import re

# ============================
# ROMAN NUMERAL REGEX:
# ============================
regex_pattern = r"^(M){0,3}(CM)?(CD|D)?(C){0,3}(XC)?(XL|L)?(X){0,3}(IX)?(IV|V)?(I){0,3}$"

# ============================
# EXPLANATION OF PATTERN:
# ============================
#
# ^ → start of string
# $ → end of string
#
# Breakdown:
#
# M{0,3}   → 1000s (0–3000)
# CM       → 900
# CD|D     → 400 or 500
# C{0,3}   → 100s (0–300)
# XC       → 90
# XL|L     → 40 or 50
# X{0,3}   → 10s (0–30)
# IX       → 9
# IV|V     → 4 or 5
# I{0,3}   → 1s (0–3)
#
# ============================
# WHY THIS WORKS:
# ============================
#
# ✔ Enforces Roman order
# ✔ Prevents invalid repetition
# ✔ Handles subtractive rules
#
# ============================

# Example usage:
def is_valid_roman(s: str) -> bool:
    return bool(re.match(regex_pattern, s))