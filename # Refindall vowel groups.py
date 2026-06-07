# ============================
# PLATFORM:
# HackerRank
# (Regex - Re.findall: Vowel Groups)
# ============================

# ============================
# PROBLEM:
# ============================
#
# Given a string, find all substrings that:
#
# ✔ contain ONLY vowels (aeiou)
# ✔ length >= 2
# ✔ are surrounded by consonants
#
# If none exist → print -1
#
# ============================
# APPROACH:
# ============================
#
# Use REGEX with:
#
# 1. Lookbehind → consonant before
# 2. Vowel group → [aeiou]{2,}
# 3. Lookahead → consonant after
#
# ============================

import re

# ============================
# REGEX BREAKDOWN:
# ============================
#
# (?<=[qwrtypsdfghjklzxcvbnm])
#   → previous character must be consonant
#
# ([aeiou]{2,})
#   → capture 2 or more vowels
#
# (?=[qwrtypsdfghjklzxcvbnm])
#   → next character must be consonant
#
# re.IGNORECASE → case insensitive
#
# ============================

storage = re.findall(
    r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])',
    input().strip(),
    re.IGNORECASE
)

# ============================
# OUTPUT LOGIC
# ============================
if storage:
    for v in storage:
        print(v)
else:
    print(-1)