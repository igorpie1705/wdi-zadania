tab = [2, 5, 7, 3, 2, 3, 5, 7, 1, 9, 15, 21, 17, 19, 23, 2, 6, 4, 8, 5, 6, 7, 25, 30, 35]


def sequence(t):
    n = len(t)
    for dlugosc in range(3, n // 2):
        for poczatek in range(n-1-dlugosc):
            sekwencja = True
            mnoznik = t[poczatek + dlugosc] // t[poczatek]
            for i in range(1, dlugosc):
                if t[poczatek + dlugosc + i] / t[poczatek + i] != mnoznik:
                    sekwencja = False
                    break
            if sekwencja:
                return poczatek, poczatek + dlugosc - 1


print(sequence(tab))
