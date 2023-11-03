# Zadanie 15.
# Dana jest duża tablica t.
# Proszę napisać funkcję, która zwraca informację czy w tablicy
# zachodzi następujący warunek: „wszystkie elementy,
# których indeks jest elementem ciągu Fibonacciego są liczbami złożonymi,
# a wśród pozostałych przynajmniej jedna jest liczbą pierwszą”

from math import sqrt


def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def algorytm(t):
    pass