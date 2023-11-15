# Zadanie 11.
# Dwie liczby naturalne są
# „przyjaciółkami jeżeli zbiory cyfr z których zbudowane są liczby są identyczne.
# Na przykład: 123 i 321, 211 i 122, 35 3553.
# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi.
# Proszę napisać funkcję, która dla tablicy T zwraca ile elementów tablicy
# sąsiaduje wyłącznie z przyjaciółkami

from random import randint
from math import log10

n = 10
tab = [[randint(1, 2) for _ in range(n)] for _ in range(n)]

for i in tab:
    print(i)


def are_friends(a, b):
    T = [0 for _ in range(10)]
    n = len(T)
    while a >= 1:
        num = a % 10
        T[num] = 1
        a //= 10
    while b >= 1:
        num = b % 10
        if T[num] != 0:
            T[num] = 2
        else:
            return False
        b //= 10
    for i in range(n):
        if T[i] == 1:
            return False
    return True


def side(T, i, j):
    n = len(T)
    sides = [(-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]
    for k in sides:
        if 0 <= i + k[0] < n and 0 <= j + k[1] < n:
            if not are_friends(T[i][j], T[i + k[0]][j + k[1]]):
                return False
    return True


def zad11(T):
    n = len(T)
    cnt = 0
    for i in range(n):
        for j in range(n):
            if side(T, i, j):
                cnt += 1
        return cnt


print(zad11(tab))
