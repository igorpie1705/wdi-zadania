# Zadanie 16.
# Liczba Smitha to taka,
# której suma cyfr jest równa sumie cyfr wszystkich liczb występujących
# w jej rozkładzie na czynniki pierwsze.
# Na przykład: 85 = 5 ∗ 17 | 8 + 5 = 5 + 1 + 7.
# Proszę napisać program wypisujący liczby Smitha mniejsze od 1000000.

from math import sqrt


def rozklad():
    for n in range(2, 1000000+1):
        liczba = n
        suma = 0
        suma_n = 0
        for i in range(2, n):
            while n % i == 0:
                czynnik = i
                while czynnik > 0:
                    suma += czynnik % 10
                    czynnik //= 10
                n //= i
        n = liczba
        while n > 0:
            suma_n += n % 10
            n //= 10
        if suma_n == suma:
            print(liczba)


rozklad()
