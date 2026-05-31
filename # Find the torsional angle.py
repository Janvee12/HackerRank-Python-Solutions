# ============================
# PLATFORM:
# HackerRank
# (Python OOP -
# Class 3: Find the Torsional Angle)
# ============================

# ============================
# PROBLEM
# ============================
#
# Given four points:
#
# A, B, C, D
#
# in 3D space,
#
# find the torsional angle
# between the planes:
#
# Plane ABC
# Plane BCD
#
# Output the angle
# in degrees rounded
# to 2 decimal places.
#
# ============================

# ============================
# MATHEMATICAL IDEA
# ============================
#
# Plane ABC has normal vector:
#
#     X = (B-A) × (C-B)
#
# Plane BCD has normal vector:
#
#     Y = (C-B) × (D-C)
#
# Once we get the two normal
# vectors, the angle between
# the planes equals the angle
# between X and Y.
#
# Formula:
#
#           X · Y
# cos θ = -----------
#         |X| |Y|
#
# Therefore:
#
# θ = acos(
#         (X·Y)
#         /
#         (|X||Y|)
#     )
#
# Convert θ from radians
# to degrees.
#
# ============================

import math


class Points(object):

    # ========================
    # Constructor
    # ========================
    def __init__(self, x, y, z):

        self.x = x
        self.y = y
        self.z = z

    # ========================
    # Vector Subtraction
    # ========================
    #
    # A - B
    #
    # (x1-x2,
    #  y1-y2,
    #  z1-z2)
    #
    # ========================
    def __sub__(self, no):

        return Points(
            self.x - no.x,
            self.y - no.y,
            self.z - no.z
        )

    # ========================
    # Dot Product
    # ========================
    #
    # a·b =
    #
    # axbx + ayby + azbz
    #
    # ========================
    def dot(self, no):

        return (
            self.x * no.x
            + self.y * no.y
            + self.z * no.z
        )

    # ========================
    # Cross Product
    # ========================
    #
    # a × b =
    #
    # (
    # aybz − azby,
    # azbx − axbz,
    # axby − aybx
    # )
    #
    # ========================
    def cross(self, no):

        return Points(
            self.y * no.z - self.z * no.y,
            self.z * no.x - self.x * no.z,
            self.x * no.y - self.y * no.x
        )

    # ========================
    # Magnitude of Vector
    # ========================
    #
    # |v|
    #
    # = √(x²+y²+z²)
    #
    # ========================
    def absolute(self):

        return math.sqrt(
            self.x ** 2
            + self.y ** 2
            + self.z ** 2
        )


# ============================
# DRIVER CODE
# ============================

if __name__ == '__main__':

    points = []

    # Read 4 points
    for _ in range(4):

        p = list(
            map(float, input().split())
        )

        points.append(p)

    a = Points(*points[0])
    b = Points(*points[1])
    c = Points(*points[2])
    d = Points(*points[3])

    # Normal vector of plane ABC
    x = (b - a).cross(c - b)

    # Normal vector of plane BCD
    y = (c - b).cross(d - c)

    # Angle between normals
    angle = math.acos(
        x.dot(y)
        /
        (x.absolute() * y.absolute())
    )

    # Convert to degrees
    print(
        "%.2f"
        % math.degrees(angle)
    )