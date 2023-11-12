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


def sprawdz(*args):
    chuj = len(args)
    pizda = 1
    for x in range(1, chuj):
        if args[x] == args[x-1]:
            pizda += 1
    if pizda == chuj:
        return True
    return False


def r(a):
    skladane = set()
    n = int(log10(a))+1
    for i in range(n):
        skladane.add(a % 10)
        a //= 10
    return skladane

def algorytm(t):
    licznik = 0
    n = len(t) - 1
    for x in range(len(t)):
        for y in range(len(t)):
            try:
                l = t[x][y-1]
            except IndexError:
                pass
            try:
                ld = t[x+1][y-1]
            except IndexError:
                pass
            try:
                d = t[x+1][y]
            except IndexError:
                pass
            try:
                pd = t[x+1][y+1]
            except IndexError:
                pass
            try:
                p = t[x][y+1]
            except IndexError:
                pass
            try:
                pg = t[x-1][y+1]
            except IndexError:
                pass
            try:
                g = t[x-1][y]
            except IndexError:
                pass
            try:
                lg = t[x-1][y-1]
            except IndexError:
                pass
            s = tab[x][y]
            if x == 0 or y == 0 or y == n or x == n:
                if x == 0 and 0 < y < n:
                    if sprawdz(r(s), r(l), r(ld), r(d), r(pd), r(p)) is True:
                        licznik += 1
                elif x == 0 and y == 0:
                    if sprawdz(r(s), r(d), r(pd), r(p)) is True:
                        licznik += 1
                elif x == 0 and y == n:
                    if sprawdz(r(s), r(l), r(ld), r(d)) is True:
                        licznik += 1
                elif x == n and y == 0:
                    if sprawdz(r(s), r(p), r(pg), r(g)) is True:
                        licznik += 1
                elif x == n and y == n:
                    if sprawdz(r(s), r(l), r(g), r(lg)) is True:
                        licznik += 1
                elif x == n and 0 < y < n:
                    if sprawdz(r(s), r(l), r(p), r(pg), r(g), r(lg)) is True:
                        licznik += 1
                elif y == 0 and 0 < x < n:
                    if sprawdz(r(s), r(d), r(pd), r(p), r(pg), r(g)) is True:
                        licznik += 1
                elif y == n and 0 < x < n:
                    if sprawdz(r(s), r(l), r(ld), r(d), r(g), r(lg)) is True:
                        licznik += 1
            else:
                if sprawdz(r(s), r(l), r(ld), r(d), r(pd), r(p), r(pg), r(g), r(lg)) is True:
                    licznik += 1
    print(licznik)


algorytm(tab)
