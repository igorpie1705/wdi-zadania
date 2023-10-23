# Zadanie 9.
# Napisać funkcję, która dla N-elementowej tablicy t
# wypełnionej liczbami naturalnym wyznacza długość najdłuższego,
# spójnego podciągu rosnącego.
# [60, 56, 16, 69, 36, 15, 79, 63, 65, 5]

from random import randint


def algorytm(n):
    t = []
    for i in range(n):
        t.append(randint(1, 100))
    cnt = 1
    max_cnt = cnt
    for i in range(1, len(t)):
        if t[i] > t[i-1]:
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
        else:
            cnt = 1
    print(t)
    print(max_cnt)


algorytm(10)


