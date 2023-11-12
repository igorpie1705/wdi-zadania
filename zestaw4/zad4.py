# Zadanie 4.
# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi.
# Proszę napisać funkcję, która zwraca wiersz i kolumnę dowolnego elementu,
# dla którego iloraz sumy elementów w kolumnie w którym leży element
# do sumy elementów wiersza w którym leży element jest największa.


from random import randint

n = 5
tab = [[randint(1, 9) for _ in range(n)] for _ in range(n) ]


def f(k, w):
    return k / w


def algorytm(t):
    n = len(t)
    maxi_suma = 0
    wsp_x = 0
    wsp_y = 0
    for wiersz in range(n):
        suma_w = 0
        for w in range(n):
            suma_w += t[wiersz][w]
        for kolumna in range(n):
            suma_k = 0
            for chuj in range(n):
                suma_k += t[chuj][kolumna]
            suma = (suma_k + t[wiersz][kolumna]) / suma_w
            if suma > maxi_suma:
                maxi_suma = suma
                wsp_x = kolumna
                wsp_y = wiersz
    print(wsp_x, wsp_y)


for i in range(len(tab)):
    print(""
          "")
    for j in range(len(tab)):
        print(tab[i][j], end=" ")
print("\n")
algorytm(tab)
