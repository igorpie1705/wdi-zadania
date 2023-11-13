# Zadanie 20. Dana jest N-elementowa tablica t zawierajaca liczby naturalne
# mniejsze od 1000. Prosze napisac
# funkcje, która zwraca długosc najdłuzszego, spójnego fragmentu tablicy,
# dla którego w iloczynie jego elementów
# kazdy czynniki pierwszy wystepuje co najwyzej raz.
# Na przykład dla tablicy t=[2,23,33,35,7,4,6,7,5,11,13,22]
# wynikiem jest wartosc 5.

from random import randint

n = 10
tab = [randint(1, 999) for i in range(n)]

t = [2, 23, 33, 35, 7, 4, 6, 7, 5, 11, 13, 22]

def is_distinct(t):
    dl = len(t)
    for i in range(dl):
        for j in range(i+1, dl):
            if t[i] == t[j]:
                return False
    return True


def rozklad(n):
    i = 2
    czynniki = []
    while n > 1:
        while n % i == 0:
            czynniki.append(i)
            n //= i
        i += 1
    return czynniki

def algorytm(t):
    dl = 0
    maxi_dl = 0
    iloczyn = 1
    for i in range(1, len(t)):
        iloczyn = iloczyn * t[i-1]
        if is_distinct(rozklad(iloczyn)):
            dl += 1
            maxi_dl = max(dl, maxi_dl)
        else:
            iloczyn = 1
            dl = 0
    print(maxi_dl)

print(tab)
algorytm(tab)
