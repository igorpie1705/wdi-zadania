# Na szachownicy o rozmiarach N × N reprezentowanej przez tablicę T[N][N] umieszczono pewną liczbę skoczków.
# Położenie skoczka w tablicy oznaczono liczbą 1, puste pola oznaczono liczbą 0. Część pustych pól na szachownicy
# jest szachowana przez znajdujące się na niej skoczki. Proszę zaproponować funkcję place(T), która znajdzie na
# szachownicy puste pole położone najbliżej środka szachownicy, takie że umieszczenie tam skoczka maksymalnie
# zwiększy liczbę szachowanych pustych pól. Do funkcji przekazujemy tablicę T zawierającą położenie skoczków. Funkcja
# powinna zwrócić pole (wiersz, kolumna), na którym należy umieścić skoczka. Odległość pomiędzy polami: (w1,
# k1) i (w2, k2) jest równa max(abs(w1 − w2), abs(k1 − k2))


tab = [
    [0, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0, 1, 1, 0]
]




def place(T):
    def ile_szachowanych(T):
        n = len(T)
        ruchy = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        cnt = 0
        for w in range(n):
            for k in range(n):
                if T[w][k] == 1:
                    for e in ruchy:
                        if 0 <= w + e[0] < n and 0 <= k + e[1] < n and T[w + e[0]][k + e[1]] != 1:
                            if T[w + e[0]][k + e[1]] == 0:
                                T[w + e[0]][k + e[1]] = 2
                                cnt += 1
        return cnt
    n = len(T)
    s = (n - 1) // 2
    srodek = T[s][s]
    max_ilosc = 0
    min_odleglosc = 0
    wsp_x = 0
    wsp_y = 0
    for w in range(n):
        for k in range(n):
            if T[w][k] == 0:
                T[w][k] = 1
                ilosc = ile_szachowanych(T)
                odl = max(abs(s - w), abs(k - s))
                if ilosc > max_ilosc:
                    max_ilosc = ilosc
                    min_odleglosc = odl
                    wsp_x = w
                    wsp_y = k
                elif ilosc == max_ilosc:
                    if odl < min_odleglosc:
                        min_odleglosc = odl
                        wsp_x = w
                        wsp_y = k
                T[w][k] = 0
    print(max_ilosc, wsp_x, wsp_y)


place(tab)