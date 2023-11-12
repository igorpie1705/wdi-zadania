# Zadanie 7.
# Dane są dwie tablice mogące pomieścić taką samą liczbę elementów:
# T1[N][N] i T2[M], gdzie M=N*N.
# W każdym wierszu tablicy T1 znajdują się uporządkowane niemalejąco
# (w obrębie wiersza) liczby naturalne.
# Proszę napisać funkcję przepisującą wszystkie liczby z tablicy T1 do T2,
# tak aby liczby w tablicy T2 były uporządkowane niemalejąco.

from random import randint

n = 3
tab = [[randint(1, 100) for _ in range(n)] for _ in range(n)]

tab2 = [0] * n * n

for wiersz in tab:
    wiersz.sort()

print(tab)