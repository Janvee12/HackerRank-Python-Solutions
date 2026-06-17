# ============================
# PLATFORM:
# HackerRank
# (HTML Parser - Part 1)
# ============================

# ============================
# PROBLEM:
# ============================
#
# You are given HTML input.
# You need to parse it and print:
#
# 1. Start tags
# 2. End tags
# 3. Empty (self-closing) tags
#
# Also print attributes of tags.
#
# ============================
# APPROACH:
# ============================
#
# We use Python's built-in:
#
#   HTMLParser
#
# and override:
#
# - handle_starttag
# - handle_endtag
# - handle_startendtag
#
# ============================

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    # ============================
    # START TAG
    # ============================
    def handle_starttag(self, tag, attrs):
        print('Start :', tag)

        for attr in attrs:
            print('->', attr[0], '>', attr[1])

    # ============================
    # END TAG
    # ============================
    def handle_endtag(self, tag):
        print('End   :', tag)

    # ============================
    # SELF-CLOSING TAG
    # ============================
    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)

        for attr in attrs:
            print('->', attr[0], '>', attr[1])


# ============================
# DRIVER CODE
# ============================

parser = MyHTMLParser()

html = ''.join(
    input().strip()
    for _ in range(int(input()))
)

parser.feed(html)