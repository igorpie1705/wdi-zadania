# Zadanie 11.
# Proszę napisać program wczytujący liczbę naturalną
# i odpowiadający na pytanie, czy jej cyfry stanowią ciąg rosnący.

from math import log10


# 4567
def algorytm(n):
    dl = round(log10(n))
    for i in range(dl-1):
        a = n % 10
        n //= 10
        b = n % 10
        if a - b <= 0:
            print("NIE")
            return
    print("TAK")
    return


algorytm(123456789)
