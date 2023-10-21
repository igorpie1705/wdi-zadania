# Zadanie 20.
# Dwie liczby naturalne są różno-cyfrowe
# jeżeli nie posiadają żadnej wspólnej cyfry.
# Proszę napisać program, który wczytuje dwie liczby naturalne
# i poszukuje najmniejszej podstawy systemu (w zakresie 2 − 16)
# w którym liczby są różno-cyfrowe.
# Program powinien wypisać znalezioną podstawę,
# jeżeli podstawa taka nie istnieje należy wypisać komunikat o jej braku.
# Na przykład: dla liczb 123 i 522 odpowiedzią jest podstawa
# 11 bo 123(10) = 102(11) i 522(10) = 435(11).


def zamien(n, p):
    liczba = ''
    if p == 1:
        return n
    while n > 0:
        dodaj = n % p
        n //= p
        if dodaj >= 10:
            dodaj -= 10
            liczba += chr(ord('A') + dodaj)
        else:
            liczba += str(dodaj)
    return liczba[::-1]


def algorytm(a, b):
    i = 1
    while i <= 16:
        rozno = True
        liczba_a = str(zamien(a, i))
        liczba_b = str(zamien(b, i))
        for x in liczba_a:
            if x in liczba_b:
                rozno = False
        if rozno:
            print(i)
            return
        else:
            i += 1
    print("BRAK")


algorytm(123, 522)
