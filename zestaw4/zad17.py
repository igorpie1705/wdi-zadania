# Zadanie 17.
# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi.
# Proszę napisać funkcję która zwraca wiersz i kolumnę dowolnego elementu,
# dla którego suma otaczających go elementów jest największa.

from random import randint
from math import sqrt

n = 5
tab = [[randint(1, 99) for _ in range(n)] for _ in range(n)]

for i in tab:
    print(i)
