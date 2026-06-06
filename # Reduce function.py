# ============================
# PLATFORM:
# HackerRank
# (Python - Reduce / Fractions)
# ============================

# ============================
# PROBLEM:
# ============================
#
# You are given a list of fractions.
# You need to multiply all of them
# and return result as:
#
#   numerator, denominator
#
# ============================
# APPROACH:
# ============================
#
# We use:
#   Fraction (for exact math)
#   reduce (for repeated multiplication)
#
# ============================

from fractions import Fraction
from functools import reduce


def product(fracs):
    """
    Multiply all fractions in list.
    """

    # ============================
    # STEP 1: Multiply all fractions
    # ============================
    t = reduce(lambda x, y: x * y, fracs)

    # ============================
    # STEP 2: Return numerator & denominator
    # ============================
    return t.numerator, t.denominator


# ============================
# WHY THIS WORKS:
# ============================
#
# ✔ Fraction handles simplification automatically
# ✔ reduce applies multiplication sequentially
# ✔ final result is always reduced form
#
# ============================