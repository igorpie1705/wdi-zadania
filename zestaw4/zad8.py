#
# Zadanie 8.
# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi.
# Proszę napisać funkcję, która w poszukuje w tablicy najdłuższego
# ciągu geometrycznego leżącego ukośnie w kierunku prawo-dół,
# liczącego co najmniej 3 elementy. Do funkcji należy przekazać tablicę.
# Funkcja powinna zwrócić informacje czy udało się znaleźć taki
# ciąg oraz długość tego ciągu.

from random import randint

def funkcja(t):
    maks = 0
    licznik = 1
    for i in range(0, len(t)-2):
        for j in range(0, len(t)-2):
            dl = 2
            k, w = i, j
            while tab[k][w]/tab[k+1][w+1] == tab[k+1][w+1]/tab[k+2][w+2]:
                dl += 1
                if k == len(t) - 3 or w == len(t) - 3:
                    break
                k += 1
                w += 1
            maks = max(dl, maks)
    return maks





n = 5

tab = [[randint(1, 10) for _ in range(n)] for _ in range(n)]

print(tab)
print(funkcja(tab))

