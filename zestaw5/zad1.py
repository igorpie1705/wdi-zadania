# Zadanie 1. Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
# co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej
# cyfry.

from math import sqrt


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


def zad1(num):
    num = str(num)
    n = len(num)-1

    def rek(i, liczba, tab):
        if len(liczba) < 2:
            return
        if czy_pierwsza(liczba):
            if int(liczba) not in tab:
                tab.append(int(liczba))
        for x in range(len(liczba)):
            rek(x, liczba.replace(liczba[x], ""), tab)
        return tab

    print(rek(0, num, []))


zad1(324185329238432)
