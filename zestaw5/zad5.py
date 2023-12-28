# Zadanie 5. Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
# na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość
# każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu
# 110100 nie jest możliwe.

from math import sqrt

T = [111011]


def czy_pierwsza(n):
    n = int(n)
    i = 2
    if n < 2:
        return False
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True


def bin_na_dec(binary):
    binary = int(binary)
    decimal, i = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal

def zad5(T):
    ciag = str(T[0])

    def rek(ciong):
        if len(ciong) == 1:
            return False
        if ciong != ciag and czy_pierwsza(bin_na_dec(ciong)):
            return True
        for i in range(2, len(ciong)):
            if rek(ciong[0:i]) and rek(ciong[i:]):
                return True
        return False
    return rek(ciag)


print(zad5(T))
