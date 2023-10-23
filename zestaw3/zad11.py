# Zadanie 11.
# Napisać funkcję, która dla N-elementowej tablicy t
# wypełnionej liczbami naturalnym wyznacza długość najdłuższego,
# spójnego podciągu geometrycznego.

from random import randint


def algorytm(n):
    t = [5, 3, 2, 4, 8, 16, 32]

    # for i in range(n):
    #     t.append(randint(1, 100))
    cnt = 1
    max_cnt = cnt
    q = 0
    for i in range(1, len(t)):
        if q == 0:
            q = t[i] / t[i - 1]
            i += 1
        if t[i] / t[i - 1] == q:
            cnt += 1
            if cnt > max_cnt:
                max_cnt = cnt
        else:
            q = 0
            cnt = 1
    print(t)
    print(max_cnt)


algorytm(10)
