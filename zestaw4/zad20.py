# Zadanie 20.
# Dana jest tablica T[N][N] (reprezentująca szachownicę)
# wypełniona liczbami naturalnymi.
# Proszę napisać funkcję która ustawia na szachownicy dwie wieże,
# tak aby suma liczb na „szachowanych” przez wieże polach była największa.
# Do funkcji należy przekazać tablicę, funkcja powinna zwrócić położenie wież.
# Uwaga- zakładamy, że wieża szachuje cały wiersz i kolumnę
# z wyłączeniem pola na którym stoi

from random import randint

n = 8
tab = [[randint(1, 99) for _ in range(n)] for _ in range(n)]

for i in tab:
    print(i)


def sum_of_col(t, c):
    sum = 0
    for i in range(len(t)):
        sum += t[i][c]
    return sum


def sum_of_row(t, r):
    sum = 0
    for i in range(len(t)):
        sum += t[r][i]
    return sum


def main(t):
    maxi = 0
    b_indx, b_indy, c_indx, c_indy = 0, 0, 0, 0
    n = len(t)
    for r in range(n):
        for c in range(n):
            for y in range(n):
                for x in range(n):
                    if c != x and r != y:
                        suma = sum_of_row(t, r) + sum_of_col(t, c) + sum_of_row(t, y) + sum_of_col(t, x) - 2 * t[x][
                            y] - 2 * t[r][c] - t[r][x] - t[y][c]
                        if suma > maxi:
                            maxi = suma
                            b_indx, b_indy = c, r
                            c_indx, c_indy = x, y
    return [(b_indx, b_indy), (c_indx, c_indy)]


print(main(tab))
