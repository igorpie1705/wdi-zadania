# Zadanie 13.
# Proszę napisać program, który wypełnia N-elementową tablicę
# t trzycyfrowymi liczbami pseudolosowymi,
# a następnie wyznacza i wypisuje długość najdłuższego podciągu spójnego
# znajdującego się w tablicy dla którego w tablicy występuje
# również rewers tego ciągu.
# Na przykład dla tablicy: t= [2,9,3,1,7,11,9,6,7,7,1,3,9,12,15]
# odpowiedzią jest liczba 4.

from random import randint


def algorytm(t):
    tab = []
    max_licznik = 0
    for i in range(t):
        tab.append(randint(1, 100))
    for i in range(1, len(tab)):
        licznik = 0
        for j in range(len(tab)-1, 0, -1):
            while tab[i] == tab[j] and i < j:
                licznik += 1
                if licznik > max_licznik:
                    max_licznik = licznik
                i += 1
                j -= 1
    print(tab)
    print(max_licznik)


algorytm(100)

