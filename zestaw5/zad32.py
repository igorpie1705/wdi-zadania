# Zadanie 32. Dana jest tablica T[N] zawierająca liczby naturalne. Proszę napisać funkcję, która odpowiada
# na pytanie, czy spośród (niekoniecznie wszystkich) elementów tablicy można utworzyć dwa podzbiory o
# jednakowej sumie elementów, tak aby suma mocy obu podzbiorów wynosiła k. Do funkcji należy przekazać
# wyłącznie tablicę T oraz liczbę naturalną k, funkcja powinna zwrócić wartość typu bool.


T = [3, 5, 1, 3, 32, 18, 53, 21, 57, 3]


def sumuj(t):
    suma = 0
    for i in t:
        suma += i
    return suma

def zad32(T, k):
    n = len(T)

    def rek(i, a, b):
        if sumuj(a) == sumuj(b) and len(a) == len(b) == k:
            print(a, b)
            return True
        if i == n:
            return False

        if rek(i + 1, a, b + [T[i]]) or rek(i + 1, a + [T[i]], b) or rek(i + 1, a, b):
            return True
        return False

    return rek(0, [], [])


print(zad32(T, 5))
