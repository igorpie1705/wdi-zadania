# Zadanie 10.
# Napisać funkcję która dla tablicy T[N][N],
# wypełnionej liczbami całkowitymi, zwraca wartość True w przypadku,
# gdy w każdym wierszu i każdej kolumnie występuje co najmniej jedno 0
# oraz wartość False w przeciwnym przypadku.

from random import randint

n = 5
tab = [[randint(0, 2) for _ in range(n)] for _ in range(n)]

for i in tab:
    print(i)


def algorytm(t):
    for wiersz in t:
        if 0 not in wiersz:
            print("NIE")
            return False
    for y in range(0, len(t)):
        istnieje = False
        for x in range(0, len(t)):
            if t[x][y] == 0:
                istnieje = True
                break
        if istnieje is False:
            print("NIE")
            return False
    print("TAK")
    return True


algorytm(tab)