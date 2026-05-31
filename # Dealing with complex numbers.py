# ============================
# PLATFORM:
# HackerRank
# (Python OOP - Classes:
#  Dealing with Complex Numbers)
# ============================

# ============================
# PROBLEM:
#
# Implement a Complex class
# supporting:
#
# + Addition
# + Subtraction
# + Multiplication
# + Division
# + Modulus
#
# and print results in the
# required format.
#
# Complex Number:
#
#     a + bi
#
# where:
#
# a = real part
# b = imaginary part
# ============================

# ============================
# FORMULAS
# ============================
#
# Addition:
#
# (a+bi)+(c+di)
#
# = (a+c)+(b+d)i
#
# ----------------------------
#
# Subtraction:
#
# (a+bi)-(c+di)
#
# = (a-c)+(b-d)i
#
# ----------------------------
#
# Multiplication:
#
# (a+bi)(c+di)
#
# = ac + adi + bci + bd(i²)
#
# Since:
#
# i² = -1
#
# = (ac-bd)+(ad+bc)i
#
# ----------------------------
#
# Division:
#
#          a+bi
# ---------------------
#          c+di
#
# Multiply numerator and
# denominator by conjugate:
#
# c-di
#
# Result:
#
# Real:
#
# (ac+bd)/(c²+d²)
#
# Imaginary:
#
# (bc-ad)/(c²+d²)
#
# ----------------------------
#
# Modulus:
#
# |a+bi|
#
# = √(a²+b²)
#
# ============================

import math

class Complex(object):

    # Constructor
    def __init__(self, real, imaginary):

        self.real = real
        self.imaginary = imaginary

    # ========================
    # Addition
    # ========================
    def __add__(self, no):

        return Complex(
            self.real + no.real,
            self.imaginary + no.imaginary
        )

    # ========================
    # Subtraction
    # ========================
    def __sub__(self, no):

        return Complex(
            self.real - no.real,
            self.imaginary - no.imaginary
        )

    # ========================
    # Multiplication
    # ========================
    def __mul__(self, no):

        real_part = (
            self.real * no.real
            - self.imaginary * no.imaginary
        )

        imaginary_part = (
            self.real * no.imaginary
            + self.imaginary * no.real
        )

        return Complex(
            real_part,
            imaginary_part
        )

    # ========================
    # Division
    # ========================
    def __truediv__(self, no):

        denominator = (
            no.real ** 2
            + no.imaginary ** 2
        )

        numerator = self * Complex(
            no.real,
            -no.imaginary
        )

        return Complex(
            numerator.real / denominator,
            numerator.imaginary / denominator
        )

    # ========================
    # Modulus
    # ========================
    def mod(self):

        value = (
            self.real ** 2
            + self.imaginary ** 2
        )

        return Complex(
            math.sqrt(value),
            0
        )

    # ========================
    # String Formatting
    # ========================
    def __str__(self):

        if self.imaginary == 0:

            result = "%.2f+0.00i" % self.real

        elif self.real == 0:

            if self.imaginary >= 0:

                result = (
                    "0.00+%.2fi"
                    % self.imaginary
                )

            else:

                result = (
                    "0.00-%.2fi"
                    % abs(self.imaginary)
                )

        elif self.imaginary > 0:

            result = (
                "%.2f+%.2fi"
                % (self.real, self.imaginary)
            )

        else:

            result = (
                "%.2f-%.2fi"
                % (self.real, abs(self.imaginary))
            )

        return result


# ============================
# Driver Code
# ============================

if __name__ == '__main__':

    c = map(float, input().split())
    d = map(float, input().split())

    x = Complex(*c)
    y = Complex(*d)

    print(
        *map(
            str,
            [
                x + y,      # Addition
                x - y,      # Subtraction
                x * y,      # Multiplication
                x / y,      # Division
                x.mod(),    # Modulus of x
                y.mod()     # Modulus of y
            ]
        ),
        sep='\n'
    )