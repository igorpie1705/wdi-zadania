# Zadanie 3.
# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi.
# Proszę napisać funkcję, która odpowiada na pytanie,
# czy istnieje wiersz w tablicy w którym każda z liczb
# zawiera przynajmniej jedna cyfrę parzystą.

from random import randint

n = 3
tab = [[randint(1, 10) for _ in range(n)] for _ in range(n) ]


def czy_ma_cyfre_parzysta(liczba):
    liczba = str(liczba)
    for i in liczba:
        if int(i) % 2 == 0:
            return True
    return False

def algorytm(t):
    for wiersz in t:
        parzysta = False
        for wyraz in wiersz:
            if czy_ma_cyfre_parzysta(wyraz):
                parzysta = True
        if parzysta is False:
            print("NIE")
            return False
    print("TAK")
    return True


print(tab)
algorytm(tab)
