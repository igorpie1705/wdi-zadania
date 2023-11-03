# Zadanie 1. Dana jest tablica T[N][N]. Proszę napisać funkcję wypełniającą tablicę kolejnymi liczbami
# naturalnymi po spirali.


tab = []


def algorytm(t):
    for i in range(3):
        pom = []
        for j in range(3):
            pom.append(j)
        t.append(pom)
    return t


print(algorytm(tab))
