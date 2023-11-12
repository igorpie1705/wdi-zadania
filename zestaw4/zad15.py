# Zadanie 15.
# Dana jest tablica T[N][N],
# wypełniona liczbami naturalnymi. Proszę napisać funkcję,
# która odpowiada na pytanie, czy w tablicy istnieje wiersz,
# w którym każda liczba zawiera co najmniej jedną cyfrę będącą liczbą pierwszą?

from random import randint
from math import sqrt, log10

n = 3
tab = [[randint(1, 999) for _ in range(n)] for _ in range(n)]

for i in tab:
    print(i)

def pierwsza(n):
    if n < 2:
        return False
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

def sprawdz(n):
    dl = int(log10(n))+1
    for i in range(dl):
        if pierwsza(n%10):
            return True
        n //= 10
    return False


def algorytm(t):
    for wiersz in t:
        suka = True
        for liczba in wiersz:
            if sprawdz(liczba) is False:
                suka = False
                break
        if suka:
            print("TAK")
            return True
    print("NIE")
    return False


algorytm(tab)