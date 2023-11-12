# Zadanie 20.
# Dana jest tablica T[N][N] (reprezentująca szachownicę)
# wypełniona liczbami naturalnymi.
# Proszę napisać funkcję która ustawia na szachownicy dwie wieże,
# tak aby suma liczb na „szachowanych” przez wieże polach była największa.
# Do funkcji należy przekazać tablicę, funkcja powinna zwrócić położenie wież.
# Uwaga- zakładamy, że wieża szachuje cały wiersz i kolumnę
# z wyłączeniem pola na którym stoi

from random import randint


def algorytm(t, r1, r2, l1, l2):
    n = len(t)
    sum = 0
    for i in range(n):
        for j in range(n):
            if i != r1 and i != r2 and j != l1 and i != l2:
                sum += t[i][j]
        return sum

def zad20(t):
    n = len(t)
    algorytm(t, -1, -1, -1, -1)
    maxs = 0
    maxl = -1
    maxj = -1
    maxr = -1
    maxw = -1
    for i in range(n):
        for j in range(n):
            for r in range():
                pass


n = 5
tab = [[randint(1, 10) for _ in range(n)] for _ in range(n)]

