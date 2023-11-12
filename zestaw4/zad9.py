# Zadanie 9.
# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi.
# Proszę napisać funkcję, która w poszukuje w tablicy kwadratu
# o liczbie pól będącej liczbą nieparzystą większą od 1,
# którego iloczyn 4 pól narożnych wynosi k.
# Do funkcji należy przekazać tablicę i wartość k.
# Funkcja powinna zwrócić informacje czy udało się znaleźć kwadrat oraz współrzędne
# (wiersz, kolumna) środka kwadratu.

from random import randint

n = 10
tab = [[randint(1, 9) for _ in range(n)] for _ in range(n)]

for i in tab:
    print(i)


def algorytm(t, k):
    iloczyn = 1
    x = 0
    y = 2
    while y < len(t):
        while x + y < len(t):
            w = 0
            while y + w < len(t):
                iloczyn = t[x][w] * t[x][y+w] * t[y+x][w] * t[y+x][y+w]
                if iloczyn == k:
                    print(t[x][w], t[x][y + w], t[y + x][w], t[y + x][y + w])
                    print(f'({(w + y + w)//2},{(x + y + x) // 2})')
                    return 0
                w += 1
            x += 1
        y += 2
        x = 0


algorytm(tab, 1512)
