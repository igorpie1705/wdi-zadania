# Zadanie 18. Dana jest N-elementowa tablica t jest wypełniona liczbami naturalnymi. Prosze napisac
# funkcje, która zwraca długosc najdłuzszego spójnego podciagu bedacego palindromem złozonym wyłacznie
# z liczb nieparzystych. Do funkcji nalezy przekazac tablice, funkcja powinna zwrócic długosc znalezionego
# podciagu lub wartosc 0 jezeli taki podciag nie istnieje.

tab = [3, 2, 6, 3, 5, 3, 5, 4, 9, 1, 2, 3, 4, 9]


def czy_palindrom_nieparz(n):
    if n[len(n)//2] % 2 == 0:
        return False
    for i in range(len(n)//2):
        if n[i] % 2 != 1 or n[-1-i] != n[i]:
            return False
    print(n)
    return True

# tab = [3, 2, 6, 3, 1, 6, 9, 7, 5, 7, 9, 1, 2, 3, 4, 9]


print(tab[0:4])


def algorytm(t):
    maxi_dl = 0
    print(len(t))
    for i in range(len(t)):
        for j in range(len(t)-1, i, -1):
            if t[i] == t[j]:
                print(t[i:j+1])
                if czy_palindrom_nieparz(t[i:j+1]) is True:
                    if len(t[i:j+1]) > maxi_dl:
                        maxi_dl = len(t[i:j+1])
    print(maxi_dl)


algorytm(tab)
