# Zadanie 21. Tablica T[8][8] zawiera liczby naturalne. Prosze napisac funkcje, która sprawdza czy mozna
# wybrac z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby zadne dwa wybrane
# elementy nie lezały w tej samej kolumnie ani wierszu. Do funkcji nalezy przekazac wyłacznie tablice oraz
# wartosc sumy, funkcja powinna zwrócic wartosc typu bool.


T = [
    [24, 32, 12, 43, 23, 42, 23, 53],
    [53, 33, 12, 43, 63, 42, 12, 12],
    [31, 32, 63, 53, 13, 42, 23, 83],
    [24, 32, 52, 43, 23, 62, 65, 35],
    [74, 32, 17, 43, 73, 42, 45, 28],
    [24, 32, 92, 43, 23, 42, 82, 42],
    [12, 32, 42, 43, 83, 32, 92, 21],
    [54, 32, 22, 43, 13, 22, 12, 27],
]


def zad21(T, suma):
    n = len(T)

    def rek(t, s):
        if s == suma:
            return True
        if len(t) == 0:
            return False
        new_t = []
        for m in range(len(t)):
            for i in range(1, len(t)):
                if m == len(t):
                    new_t += [t[i][:m]]
                else:
                    new_t += [t[i][:m] + t[i][m + 1:]]
            print(t)
            for x in new_t:
                print(x)
            if rek(new_t, suma + t[0][m]):
                return True
        return False

    return rek(T, 0)


print(zad21(T, 89))
