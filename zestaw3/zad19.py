# Zadanie 19. Dana jest N-elementowa tablica t wypełniona liczbami naturalnymi. Prosze napisac funkcje,
# która zwraca długosc najdłuzszego, spójnego podciagu rosnacego dla którego suma jego elementów jest
# równa sumie indeksów tych elementów. Do funkcji nalezy przekazac tablice, funkcja powinna zwrócic długosc
# znalezionego podciagu lub wartosc 0 jezeli taki podciag nie istnieje.


tab = [5, 1, 2, 3, 1, 1, 6, 7, 12, 12]


def algorytm(t):
    m_dlugosc = 0
    ciag = False
    for i in range(1, len(t)):
        if ciag is False:
            dlugosc = 1
            suma = t[i - 1]
            suma_indeksow = i-1
        if t[i] > t[i-1]:
            ciag = True
            suma += t[i]
            suma_indeksow += i
            dlugosc += 1
        else:
            ciag = False
        if suma_indeksow == suma:
            if dlugosc > m_dlugosc:
                m_dlugosc = dlugosc
    print(tab)
    print(m_dlugosc)


algorytm(tab)
