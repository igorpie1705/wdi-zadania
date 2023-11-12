# Zadanie 13.
# Liczby naturalne a,b są komplementarne jeżeli ich suma jest liczbą pierwszą.
# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi.
# Proszę napisać funkcję, która zeruje elementy nie posiadające liczby komplementarnej.

from random import randint
from math import sqrt

n = 5
tab = [[randint(1, 99) for _ in range(n)] for _ in range(n)]

for i in tab:
    print(i)
print()


def pierwsza(n):
    if n < 2:
        return False
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


def komplementarna(a, b):
    suma = a + b
    if pierwsza(suma):
        return True
    return False


def algorytm(t):
    for i in range(len(t)):
        for j in range(len(t)):
            for k in range(i, len(t)):
                for l in range(j, len(t)):
                    if komplementarna(t[i][j], t[k][l]):
                        t[i][j] = 0
                        t[k][l] = 0
    for wiersz in t:
        print(wiersz)


algorytm(tab)