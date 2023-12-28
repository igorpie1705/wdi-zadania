# Zadanie 20.
# Zadanie jak powyżej. Funkcja powinna dostarczyć drogę króla w postaci tablicy zawierającej
# kierunki (liczby od 0 do 7) poszczególnych ruchów króla do wybranego celu.


from math import log10


def check_if_closer(w, k, wk, kk, move):
    return (w + move[0] - wk) ** 2 + (k + move[1] - kk) ** 2 < (w - wk) ** 2 + (k - kk) ** 2


def zad18(T, w, k):
    n = len(T)
    M = [[-1 for _ in range(n)] for _ in range(n)]
    moves = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    end_corners = [(0, 0), (0, n - 1), (n - 1, 0), (n - 1, n - 1)]

    def rek(w, k, ec):
        wk = ec[0]
        kk = ec[1]
        if w == wk and k == kk:
            return True
        else:
            for i in range(8):
                e = moves[i]
                if 0 <= w + e[0] < n and 0 <= k + e[1] < n and w + e[0] and check_if_closer(w, k, wk, kk, e):
                    next_n = T[w + e[0]][k + e[1]]
                    if T[w][k] % 10 < next_n // 10 ** (int(log10(next_n))):
                        if rek(w + e[0], k + e[1], ec):
                            M[w][k] = i
                            return True
            return False
    for ec in end_corners:
        if rek(w, k, ec):
            for e in M:
                print(e)
            return True
    return False


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

print(zad18(T, 0, 6))
