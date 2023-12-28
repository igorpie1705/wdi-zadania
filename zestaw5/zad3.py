# Zadanie 3. Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi zawierającymi
# koszt przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i kolumnie k. Król musi w
# dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy minimalny koszt przejścia króla.
# Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt przebywania na polu startowym i ostatnim także
# wliczamy do kosztu przejścia.


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


def zad3(k, t):
    n = 8
    ruchy = [(0, -1), (0, 1), (1, -1), (1, 1), (1, 0)]

    def rek(i, suma, sumy, wiersz, kol):
        if i == n - 1:
            if wiersz == 6:
                sumy += [suma]
            return

        for e in ruchy:
            if 0 <= wiersz + e[0] < 8 and 0 <= kol + e[1] < 8:
                rek(i+1, suma + t[wiersz+e[0]][kol+e[1]], sumy, wiersz + e[0], kol + e[1])
        return sumy
    return min(rek(0, t[0][k], [], 0, k))


print(zad3(4, T))