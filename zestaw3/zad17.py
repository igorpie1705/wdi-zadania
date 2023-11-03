# Zadanie 17. Dane sa dwie N-elementowe tablice t1 i t2 zawierajace liczby naturalne. Z wartosci w obu
# tablicach mozemy tworzyc sumy. „Poprawna” suma to taka, która zawiera co najmniej jeden element (z
# tablicy t1 lub t2) o kazdym indeksie. Na przykład dla tablic: t1 = [1,3,2,4] i t2 = [9,7,4,8] poprawnymi
# sumami sa na przykład 1+3+2+4, 9+7+4+8, 1+7+3+8, 1+9+7+2+4+8. Prosze napisac funkcje generujaca
# i wypisujaca wszystkie poprawne sumy, które sa liczbami pierwszymi. Do funkcji nalezy przekazac dwie
# tablice, funkcja powinna zwrócic liczbe znalezionych i wypisanych sum.

from math import sqrt

tab1 = [1, 3, 2, 4]
tab2 = [9, 7, 4, 8]


def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

# NIEWYKONALNE
