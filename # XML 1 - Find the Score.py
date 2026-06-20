# ============================
# PLATFORM:
# HackerRank
# (XML 1 - Find the Score)
# ============================

# ============================
# PROBLEM:
# ============================
#
# Given an XML document,
# count the total number
# of attributes present in
# all XML tags.
#
# ============================

# ============================
# APPROACH:
# ============================
#
# Every XML node contains:
#
#     node.attrib
#
# which stores all attributes
# of that tag.
#
# Steps:
#
# 1. Count attributes of the
#    current node.
#
# 2. Recursively visit all
#    child nodes.
#
# 3. Add their attribute counts.
#
# ============================

import sys
import xml.etree.ElementTree as etree


def get_attr_number(node):

    # Count attributes of current node
    score = len(node.attrib)

    # Visit all child nodes
    for child in node:
        score += get_attr_number(child)

    return score


if __name__ == '__main__':

    sys.stdin.readline()

    xml = sys.stdin.read()

    tree = etree.ElementTree(
        etree.fromstring(xml)
    )

    root = tree.getroot()

    print(get_attr_number(root))