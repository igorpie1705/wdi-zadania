# Zadanie 12.
# Proszę napisać program wczytujący liczbę naturalną
# i odpowiadający na pytanie, czy liczba ta zawiera cyfrę równą liczbie swoich cyfr.

from math import log10


def algorytm(n):
    dl = round(log10(n))
    for i in range(dl):
        a = n % 10
        n //= 10
        if a == dl:
            print("TAK")
            return
    print("NIE")
    return


algorytm(464123957)
