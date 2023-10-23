# Zadanie 7.
# Napisać program wypełniający N-elementową tablicę
# t liczbami pseudolosowymi z zakresu 1-1000
# i sprawdzający, czy istnieje element tablicy zawierający wyłącznie cyfry nieparzyste.

from random import randint
from math import log10


def algorytm(n):
    tab = []
    for i in range(n):
        tab.append(randint(1, 1000))
    for liczba in tab:
        tylko_nieparzyste = True
        for i in range(round(log10(liczba))):
            a = liczba % 10
            liczba //= 10
            if a % 2 == 0:
                tylko_nieparzyste = False
                break
        if tylko_nieparzyste:
            print("TAK")
            print(tab)
            return 0
    print("NIE")
    print(tab)
    return 0


algorytm(3)
