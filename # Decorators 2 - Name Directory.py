# ============================
# PLATFORM:
# HackerRank
# PROBLEM:
# Standardize Mobile Number Using Decorators
# (Person Lister)
# ============================

import operator

def person_lister(f):
    def inner(people):

        # Sort people according to age
        people = sorted(people, key=lambda x: int(x[2]))

        # Apply function to every person
        return [f(person) for person in people]

    return inner


@person_lister
def name_format(person):
    title = "Mr." if person[3] == "M" else "Ms."
    return title + " " + person[0] + " " + person[1]