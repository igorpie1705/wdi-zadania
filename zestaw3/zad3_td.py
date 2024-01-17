# Zadanie 3.
# Napisać program generujący i wypisujący liczby pierwsze mniejsze
# od N metodą Sita Eratostenesa.

from math import sqrt


def sito(n):
    pierwsza = [True for i in range(n+1)]
    p = 2
    while p <= sqrt(n):
        if pierwsza[p] is True:
            for i in range(p*p, n+1, p):
                pierwsza[i] = False
        p += 1

    for p in range(2, n+1):
        if pierwsza[p]:
            print(p)


sito(100)
