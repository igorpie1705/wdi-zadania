# Zadanie 16.
# Dana jest tablica T[N][N], wypełniona liczbami naturalnymi.
# Proszę napisać funkcję która odpowiada na pytanie,
# czy w tablicy każdy wiersz zawiera co najmniej jedną liczbą złożoną
# wyłącznie z cyfr będących liczbami pierwszymi?

from random import randint
from math import sqrt

n = 5
tab = [[randint(1, 99) for _ in range(n)] for _ in range(n)]

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


def rozloz_nozki(n):
    i = 2
    if n == 1:
        return False
    while n > 1:
        if n % i == 0:
            if pierwsza(n) is False:
                return False
            n //= i
        i += 1
    return True


def algorytm(t):
    for wiersz in t:
        femboy = False
        for liczba in wiersz:
            if rozloz_nozki(liczba):
                femboy = True
        if femboy is False:
            print("SUKA BLYEAT")
            return False
    print("LESSFUCKINGGOOOOOO")
    return True



algorytm(tab)
