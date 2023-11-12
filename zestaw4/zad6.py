# Zadanie 6.
# Dane są dwie tablice mogące pomieścić taką samą liczbę elementów:
# T1[N][N] i T2[M], gdzie M=N*N. W każdym wierszu tablicy T1 znajdują
# się uporządkowane rosnąco (w obrębie wiersza) liczby naturalne.
# Proszę napisać funkcję przepisującą wszystkie singletony
# (liczby występujące dokładnie raz) z tablicy T1 do T2,
# tak aby liczby w tablicy T2 były uporządkowane rosnąco.
# Pozostałe elementy tablicy T2 powinny zawierać zera.

from random import randint

n = 5
tab = [[randint(1, 100) for _ in range(n)] for _ in range(n)]

tab2 = [0] * n * n

pom = []

for i in tab:
    i.sort()

print(tab)

for wiersz in tab:
    for element in wiersz:
        if element not in pom:
            pom.append(element)
pom = sorted(pom)

for i in range(len(pom)):
    tab2[i] = pom[i]

print(tab2)
