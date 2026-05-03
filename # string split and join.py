# ============================
# PLATFORM:
# HackerRank (Python - Strings)
# ============================

# ============================
# PROBLEM (String Split and Join):
# Given a string, split the string on spaces and
# join it back using a hyphen (-).
#
# Example:
# Input: "this is a string"
# Output: "this-is-a-string"
# ============================

# ============================
# APPROACH:
# 1. Use split(' ') to break the string into words.
# 2. Use join('-') to combine words with hyphen.
# 3. Return the modified string.
# ============================

# ============================
# TIME COMPLEXITY:
# O(n)
# → Traverses the string once
#
# SPACE COMPLEXITY:
# O(n)
# → Stores split words and new string
# ============================

def split_and_join(line):
    return '-'.join(line.split(' '))


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)