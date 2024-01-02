# Zadanie 27. Kwadrat jest opisywany czwórką liczb całkowitych (x1, x2, y1, y2), gdzie x1, x2, y1, y2 oznaczają
# proste ograniczające kwadrat x1 < x2, y1 < y2. Dana jest tablica T zawierająca opisy N kwadratów. Proszę napisać
# funkcję, która zwraca wartość logiczną True, jeśli danej tablicy można znaleźć 13 nienachodzących na siebie
# kwadratów, których suma pól jest równa 2012 i False w przeciwnym przypadku.


T = [(3, 43, 31, 71), (48, 67, 14, 33), (100, 127, 12, 39), (30, 53, 36, 59), (43, 72, 64, 93), (98, 102, 87, 91),
     (19, 26, 31, 38), (78, 96, 59, 77), (79, 88, 82, 91), (3, 35, 100, 132), (12, 15, 99, 102), (90, 104, 77, 91),
     (47, 84, 22, 59), (9, 44, 5, 40), (73, 93, 19, 39), (32, 54, 19, 41), (51, 53, 56, 58), (92, 103, 59, 70),
     (11, 40, 67, 96), (74, 90, 85, 101), (55, 74, 85, 104), (97, 105, 15, 23), (47, 48, 18, 19), (30, 46, 64, 80),
     (5, 25, 65, 85), (14, 31, 64, 81), (88, 112, 74, 98), (16, 47, 1, 32), (34, 58, 95, 119), (94, 134, 6, 46),
     (3, 21, 75, 93), (25, 48, 14, 37), (42, 78, 80, 116), (56, 61, 29, 34), (44, 47, 95, 98), (36, 76, 70, 110),
     (21, 32, 98, 109), (11, 38, 13, 40)]


def licz_pole(wsp):
    a = wsp[1] - wsp[0]
    b = wsp[3] - wsp[2]
    return a * b


def nie_nachodza(a, b):
    if a[0] > b[1] or a[1] < b[0] or a[2] > b[3] or a[3] < b[2]:
        return True
    return False


def zad27(T):
    n = len(T)
    k = 2012
    z = 13

    def rek(i, kwadraty, suma, ilosc):
        flag = True
        if suma == k and ilosc == z:
            print(kwadraty)
            return True
        if i == n:
            return False
        if len(kwadraty) == 0:
            if rek(i + 1, kwadraty + [T[i]], suma + licz_pole(T[i]), ilosc + 1) or rek(i + 1, kwadraty, suma,
                                                                                       ilosc):
                return True
        else:
            for x in kwadraty:
                if nie_nachodza(x, T[i]) is False:
                    flag = False
            if flag:
                if rek(i + 1, kwadraty + [T[i]], suma + licz_pole(T[i]), ilosc + 1) or rek(i + 1, kwadraty, suma,
                                                                                           ilosc):
                    return True
            else:
                if rek(i + 1, kwadraty, suma, ilosc):
                    return True
        return False

    return rek(0, [], 0, 0)


print(zad27(T))
