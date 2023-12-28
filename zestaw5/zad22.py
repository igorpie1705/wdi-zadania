# Zadanie 22. Dana jest tablica T[N] zawierająca liczby naturalne. Po tablicy możemy przemieszczać się
# według następującej zasady: z pola o indeksie i możemy przeskoczyć na pole o indeksie i+k, jeżeli k jest
# czynnikiem pierwszym liczby t[i] mniejszym od t[i]. Proszę napisać funkcję, która zwraca informację czy jest
# możliwe przejście z pola o indeksie 0 na pole o indeksie N-1. Funkcja powinna zwrócić liczbę wykonanych
# skoków lub wartość -1, jeżeli powyższe przejście nie jest możliwe.

from math import sqrt

T = [4, 2, 6, 6, 9, 9, 4, 6, 8, 2, 6]


def czy_pierwsza(n):
    n = int(n)
    i = 2
    if n < 2:
        return False
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


def zad22(t):
    n = len(T)
    l = 1

    def rek(i):
        nonlocal l
        if i == n - 1:
            return True
        if i > n - 1:
            return False
        w = t[i]
        for k in range(1, w):
            if w % k == 0 and czy_pierwsza(k):
                if rek(i + k):
                    l += 1
                    return True
        return False

    if rek(0) is False:
        return -1
    return l


print(zad22(T))
