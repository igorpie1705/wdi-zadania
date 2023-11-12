# Zadanie 18.
# Dana jest tablica T[N][N] wypełniona liczbami całkowitymi.
# Proszę napisać funkcję,
# która wyszuka spójny podciąg elementów leżący poziomo lub pionowo o największej sumie.
# Maksymalna długość podciągu może wynosić 10 elementów.
# Do funkcji należy przekazać tablicę T,
# funkcja powinna zwrócić sumę maksymalnego podciągu.

from random import randint
from math import sqrt

n = 25
tab = [[randint(1, 99) for _ in range(n)] for _ in range(n)]

for i in tab:
    print(i)

def algorytm(t):
    n = len(t)
    max_wiersz = 0
    max_kol = 0
    if n > 10:
        for i in range(n):
            suma_wiersz = 0
            for x in range(n-10):
                for j in range(x, x+10):
                    suma_wiersz += t[i][j]
                    max_wiersz = max(suma_wiersz, max_wiersz)
        for j in range(n):
            suma_kol = 0
            for x in range(n-10):
                for i in range(x, x+10):
                    suma_kol += t[i][j]
                    max_kol = max(suma_kol, max_kol)
    for i in range(n):
        suma_wiersz = 0
        for j in range(n):
            suma_wiersz += t[i][j]
            max_wiersz = max(suma_wiersz, max_wiersz)
    for j in range(n):
        suma_kol = 0
        for i in range(n):
            suma_kol += t[i][j]
            max_kol = max(suma_kol, max_kol)
    result = max(max_kol, max_wiersz)
    print(result)

algorytm(tab)
