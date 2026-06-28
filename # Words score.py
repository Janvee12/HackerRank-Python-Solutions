# ============================
# PLATFORM:
# HackerRank
# PROBLEM:
# Words Score
# ============================

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']


def score_words(words):
    score = 0

    for word in words:

        num_vowels = 0

        # Count vowels in the word
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1

        # Even number of vowels
        if num_vowels % 2 == 0:
            score += 2

        # Odd number of vowels
        else:
            score += 1

    return score