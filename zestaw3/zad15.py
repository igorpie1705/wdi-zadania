# Zadanie 15.
# Dana jest duża tablica t.
# Proszę napisać funkcję, która zwraca informację czy w tablicy
# zachodzi następujący warunek: „wszystkie elementy,
# których indeks jest elementem ciągu Fibonacciego są liczbami złożonymi,
# a wśród pozostałych przynajmniej jedna jest liczbą pierwszą”

from math import sqrt
from random import randint


def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def algorytm(t):
    print(t)
    dlugosc = len(t)
    fib = [0]
    a, b = 0, 1
    j = 0
    pierwsza = False
    zlozone = True
    while b < dlugosc:
        fib.append(b)
        a, b = b, a + b
    print(fib)
    for wyraz_ciagu in fib:
        for i in range(j, wyraz_ciagu):
            if czy_pierwsza(tab[i]):
                pierwsza = True
        if czy_pierwsza(tab[wyraz_ciagu]) is True:
            zlozone = False
            print("NIE")
            return 0
        j = wyraz_ciagu + 1
    if pierwsza is False:
        print("NIE")
        return 0
    print("TAK")


tab = []

for i in range(50):
    tab.append(randint(1, 100))

algorytm(tab)
