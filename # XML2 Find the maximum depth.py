# ============================
# PLATFORM:
# HackerRank
# PROBLEM:
# XML 2 - Find the Maximum Depth
# ============================

# ============================
# PROBLEM:
# ============================
#
# Given an XML tree, find the
# maximum depth of the XML.
#
# Root node is at depth 0.
#
# ============================

import xml.etree.ElementTree as etree

maxdepth = 0

def depth(elem, level):
    global maxdepth

    # Update maximum depth
    maxdepth = max(maxdepth, level)

    # Visit all child nodes
    for child in elem:
        depth(child, level + 1)


if __name__ == '__main__':
    n = int(input())

    xml = ""
    for _ in range(n):
        xml += input()

    tree = etree.ElementTree(
        etree.fromstring(xml)
    )

    root = tree.getroot()

    depth(root, 0)

    print(maxdepth)