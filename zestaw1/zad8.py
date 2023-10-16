# Zadanie 8
# Proszę napisać program sprawdzający, czy zadana liczba jest pierwszą.
from math import sqrt


def pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def pierwsza_2(n):
    if n < 2:
        return False
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


if pierwsza(797):
    print("TAK")
if pierwsza_2(797):
    print("TAK")