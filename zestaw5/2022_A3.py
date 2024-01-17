# Na szachownicy o wymiarach N × N umieszczono pewną liczbę pionków. Położenie pionków opisuje lista [(w0, k0),(w1,
# k1),(w2, k2), ...]. W lewym górnym rogu szachownicy (o współrzędnych 0, 0) znajduje się król, który musi dotrzeć do
# prawego dolnego rogu szachownicy. Król może wykonywać ruchy w prawo, w dół lub w górę szachownicy, nie może zbijać
# pionków ani wracać na pole, na którym już był. Proszę na funkcję king(N,L), która zwróci maksymalną liczbę ruchów
# jakie może wykonać król na drodze do celu. Do funkcji należy przekazać wyłącznie dwa parametry: rozmiar szachownicy
# N oraz listę L zawierającą położenia pionków. Jeżeli dotarcie do celu nie jest możliwe funkcja powinna zwrócić
# wartość None.

L = [(4, 2), (5, 1), (8, 2), (1, 2), (5, 2), (1, 9), (2, 3), (4, 5), (6, 7)]


def king(N, L):
    n = N
    ruchy = [(0, 1), (1, 0), (-1, 0)]
    max_ruchy = 0
    X = [[0 for _ in range(n)] for _ in range(n)]
    X[0][0] = 1

    def rek(i, w, k, T):
        for x in T:
            print(x)
        print()
        nonlocal max_ruchy
        if w == n-1 and k == n-1:
            if i > max_ruchy:
                print(i)
                max_ruchy = i
            return True
        for e in ruchy:
            if 0 <= w + e[0] < n and 0 <= k + e[1] < n and (w + e[0], k + e[1]) not in L and T[w + e[0]][k + e[1]] == 0:
                T[w + e[0]][k + e[1]] += 1
                rek(i + 1, w + e[0], k + e[1], T)
    rek(0, 0, 0, X)
    if max_ruchy == 0:
        return None
    return max_ruchy


print(king(8, L))
