# Zadanie 2
# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi.
# Proszę napisać funkcję, która odpowiada na pytanie,
# czy w każdym wierszu tablicy występuje co najmniej
# jedna liczba złożona wyłącznie z nieparzystych cyfr.

from random import randint


def zlozenie(n):
    i = 2
    while n > 0:
        if n % i == 0:
            if i % 2 == 0:
                return False
        n //= i
        i += 1
    return True


n = 3

tab = [[randint(1, 10) for _ in range(n)] for _ in range(n) ]

print(tab)

def algorytm(t):
    dl = 0
    for wiersz in t:
        for wyraz in wiersz:
            if zlozenie(wyraz):
                dl += 1
                break
    if dl == len(t):
        print("TAK")
    else:
        print("NIE")


algorytm(tab)

