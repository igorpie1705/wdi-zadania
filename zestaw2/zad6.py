# Zadanie 6.
# Proszę napisać program wczytujący liczbę naturalną
# i rozkładający ją na iloczyn 2 liczb o najmniejszej różnicy.
# Np. 30 = 5 ∗ 6 lub 120 = 10 ∗ 12.

from math import sqrt


def algorytm(n):
    min_roznica = n
    liczba = None
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            if n // i - i < min_roznica:
                min_roznica = n // i - i
                liczba = i
    print(liczba, n // liczba)


algorytm(120)
