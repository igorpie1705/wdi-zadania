# Zadanie 20

from math import sqrt


def algorytm(a, b):
    EPS = 1e-6
    while abs(a - b) > EPS:
        a = sqrt(a * b)
        b = (a + b) / 2
    return a


print(algorytm(12, 43))
