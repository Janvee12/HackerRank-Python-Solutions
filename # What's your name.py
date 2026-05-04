# ============================
# PLATFORM:
# HackerRank (Python - Strings / Functions)
# ============================

# ============================
# PROBLEM (What's Your Name?):
# Given the first name and last name,
# print the following message:
#
# "Hello <first_name> <last_name>! You just delved into python."
#
# Example:
# Input:
# Ross
# Taylor
#
# Output:
# Hello Ross Taylor! You just delved into python.
# ============================

# ============================
# APPROACH:
# 1. Take first name and last name as input.
# 2. Use formatted string (f-string) to insert values.
# 3. Print the required message.
# ============================

# ============================
# TIME COMPLEXITY:
# O(1)
# → Constant time operation
#
# SPACE COMPLEXITY:
# O(1)
# → No extra space used
# ============================

def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)