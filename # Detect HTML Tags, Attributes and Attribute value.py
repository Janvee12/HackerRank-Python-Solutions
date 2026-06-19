# ============================
# PLATFORM:
# HackerRank
# (Detect HTML Tags, Attributes
# and Attribute Values)
# ============================

# ============================
# PROBLEM:
# ============================
#
# Given HTML code,
# print:
#
# 1. Tag name
# 2. Attribute name
# 3. Attribute value
#
# Format:
#
# tag
# -> attribute > value
#
# ============================

# ============================
# APPROACH:
# ============================
#
# Use Python's HTMLParser.
#
# Override:
#
#     handle_starttag()
#
# Whenever a start tag is found,
# HTMLParser provides:
#
# tag   -> tag name
# attrs -> list of attributes
#
# Print them in the required
# format.
#
# ============================

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    # ============================
    # HANDLE START TAG
    # ============================
    def handle_starttag(self, tag, attrs):

        print(tag)

        self.print_attributes(attrs)

    # ============================
    # PRINT ATTRIBUTES
    # ============================
    def print_attributes(self, attrs):

        for name, value in attrs:
            print(f"-> {name} > {value}")


# ============================
# DRIVER CODE
# ============================

parser = MyHTMLParser()

for _ in range(int(input())):
    parser.feed(input())