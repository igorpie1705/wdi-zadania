# Zadanie 13.
# Proszę napisać program wczytujący liczbę naturalną
# i odpowiadający na pytanie, czy liczba zakończona jest unikalną cyfrą.


from math import log10


def algorytm(n):
    dl = round(log10(n))
    uniq = n % 10
    for i in range(dl):
        n //= 10
        a = n % 10
        if a == uniq:
            print("NIE")
            return
    print("TAK")
    return


algorytm(1464123957)
