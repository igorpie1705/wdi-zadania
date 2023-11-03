# Zadanie 12.
# Proszę napisać program, który wypełnia N-elementową tablicę
# t pseudolosowymi liczbami nieparzystymi z zakresu [1..99],
# a następnie wyznacza i wypisuje różnicę pomiędzy długością
# najdłuższego znajdującego się w niej ciągu arytmetycznego o dodatniej różnicy,
# a długością najdłuższego ciągu arytmetycznego o ujemnej różnicy,
# przy założeniu, że kolejnymi wyrazami ciągu są elementy tablicy o kolejnych indeksach.

from random import randint


def algorytm(n):
    t = []
    while len(t) <= n:
        x = randint(1, 99)
        if x % 2 == 1:
            t.append(x)
    cnt = 1
    max_cnt_ros = cnt
    max_cnt_mal = cnt
    r = 0
    for i in range(1, len(t)):
        if r == 0:
            r = t[i] - t[i - 1]
        if t[i] - t[i - 1] == r:
            cnt += 1
            if cnt > max_cnt_mal and r < 0:
                max_cnt_mal = cnt
            if cnt > max_cnt_ros and r > 0:
                max_cnt_ros = cnt
        else:
            r = 0
            cnt = 1
    print(t)
    print(max_cnt_ros, max_cnt_mal)
    print(max_cnt_ros - max_cnt_mal)


algorytm(1000)
