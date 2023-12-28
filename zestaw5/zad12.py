# Zadanie 12. Proszę zmodyfikować poprzedni program aby wypisywał znalezione n-ki.


T = [5, 1, 3, 5, 1, 9, 7, 6, 15]


def zad11(T, k):
    enki = [0] * (len(T) + 1)
    n = len(T)

    def rek(i, p):
        nonlocal enki
        if i == n:
            iloczyn = 1
            for i in p:
                iloczyn *= i
            if iloczyn == k:
                print(p)
                enki[len(p)] += 1
            return

        rek(i + 1, p)
        rek(i + 1, p + [T[i]])
        return enki

    return rek(0, [])


print(zad11(T, 150))
