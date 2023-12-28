# Zadanie 6. Dana jest tablica T [N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w sensie
# liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów tych elementów. Do
# funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego podzbioru. Na przykład dla
# tablicy: [1,7,3,5,11,2] rozwiązaniem jest liczba 10.

T = [1, 7, 3, 5, 11, 2]


def zad6(T):
    n = len(T)
    min_liczebnosc = 9999999
    min_suma = 0

    def rek(i, p, idx):
        nonlocal min_liczebnosc
        nonlocal min_suma

        if i == n:
            if len(p) > 0:
                suma = 0
                for i in p:
                    suma += i
                if suma == idx:
                    if len(p) < min_liczebnosc:
                        min_liczebnosc = len(p)
                        min_suma = suma
            return

        rek(i + 1, p, idx)
        rek(i + 1, p + [T[i]], idx + i)

        return min_suma

    return rek(0, [], 0)


print(zad6(T))
