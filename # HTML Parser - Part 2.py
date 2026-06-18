# ============================
# PLATFORM:
# HackerRank
# (HTML Parser - Part 2)
# ============================

# ============================
# PROBLEM:
# ============================
#
# Given HTML code,
# identify and print:
#
# 1. Comments
#    - Single-line comments
#    - Multi-line comments
#
# 2. Data between tags
#
# ============================

# ============================
# APPROACH:
# ============================
#
# Use Python's built-in:
#
#     HTMLParser
#
# Override:
#
#     handle_comment()
#     handle_data()
#
# HTMLParser automatically
# calls these methods when
# comments or data are found.
#
# ============================

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    # ============================
    # HANDLE COMMENTS
    # ============================
    def handle_comment(self, comment):

        if '\n' in comment:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")

        print(comment)

    # ============================
    # HANDLE DATA
    # ============================
    def handle_data(self, data):

        # Ignore blank lines
        if data == '\n':
            return

        print(">>> Data")
        print(data)


# ============================
# READ HTML INPUT
# ============================

html = ""

for _ in range(int(input())):
    html += input().rstrip()
    html += '\n'

# ============================
# PARSE HTML
# ============================

parser = MyHTMLParser()
parser.feed(html)
parser.close()