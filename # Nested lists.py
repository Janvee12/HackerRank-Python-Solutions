# ============================
# PLATFORM:
# HackerRank (Python - Nested Lists)
# ============================

# ============================
# PROBLEM (Nested Lists - Second Lowest Score):
# Given the names and scores of students, store them in a list.
#
# Then print the names of all students who have the second lowest score.
#
# Conditions:
# - If multiple students have the same second lowest score, print all names.
# - Output names should be in alphabetical order.
#
# Example:
# Input:
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
#
# Output:
# Berry
# Harry
# ============================

# ============================
# APPROACH:
# 1. Store all scores in a list (score_lst).
# 2. Store [name, score] pairs in marksheet.
# 3. Remove duplicate scores using set().
# 4. Sort the unique scores.
# 5. Pick second lowest score.
# 6. Filter names having that score.
# 7. Sort names alphabetically and print.
# ============================

# ============================
# TIME COMPLEXITY:
# O(n log n)
# → sorting scores + sorting names
#
# SPACE COMPLEXITY:
# O(n)
# → storing marksheet and scores
# ============================

if __name__ == '__main__':
    score_lst = []
    marksheet = []

    # Input collection
    for _ in range(int(input())):
        name = input()
        score = float(input())

        score_lst.append(score)
        marksheet.append([name, score])

    # Find second lowest score
    second_low = sorted(list(set(score_lst)))[1]

    # Get names with second lowest score (sorted alphabetically)
    names = [
        name
        for name, scores in sorted(marksheet)
        if scores == second_low
    ]

    # Print result
    print('\n'.join(names))