# Zadanie 3 (5 pkt)
# Na szachownicy o wymiarach N ×N wypełnionej liczbami naturalnymi > 1 odbywają się wyścigi wież.
# Pierwsza wieża startuje z lewego górnego rogu i ma dotrzeć do prawego dolnego rogu szachownicy. Pierwsza wieża może
# wykonywać tylko ruchy w prawo lub w dół szachownicy. Druga wieża startuje z prawego górnego rogu i ma dotrzeć do
# lewego dolnego rogu szachownicy. Druga wieża może wykonywać tylko ruchy w lewo lub w dół szachownicy. Wygrywa
# wieża, która dotrze do mety w mniejszej liczbie ruchów. Wieże mogą wykonać ruch z jednego pola na drugie tylko
# wtedy, gdy liczby na obu polach są względnie pierwsze. Proszę napisać funkcję, która dla danej tablicy zwraca numer
# wieży, która wygra wyścig lub 0, jeżeli wyścig będzie nierozstrzygnięty. Można założyć, że podczas wyścigu wieże
# nie spotkają się na jednym polu. Po wykonaniu funkcji zawartość tablicy nie może ulec zmianie.


from random import randint

N = 8

T = [[randint(2, 4) for i in range(N)] for x in range(N)]

for i in T:
    print(i)


def wzg_pie(a, b):
    if a > b:
        a, b = b, a
    for i in range(2, a + 1):
        if a % i == 0 and b % i == 0:
            return False
    return True


def zad3(T):
    n = len(T)
    moves1 = []
    moves2 = []
    for k in range(1, n):
        moves1 += [(0, k)]
        moves2 += [(0, -k)]
    for k in range(1, n):
        moves1 += [(k, 0)]
        moves2 += [(k, 0)]
    print(moves1)
    print(moves2)
    ruchy1 = 999999
    ruchy2 = 999999

    def rek(ruchy, wiersz, kol, wieza):
        nonlocal ruchy1, ruchy2
        if wieza == 1:
            if wiersz == n - 1 and kol == n - 1:
                if ruchy < ruchy1:
                    ruchy1 = ruchy
            for e in moves1:
                if wiersz + e[0] < n and kol + e[1] < n and wzg_pie(T[wiersz][kol], T[wiersz + e[0]][kol + e[1]]):
                    rek(ruchy + 1, wiersz + e[0], kol + e[1], 1)
            return ruchy1
        if wieza == 2:
            if wiersz == n - 1 and kol == 0:
                if ruchy < ruchy2:
                    ruchy2 = ruchy
            for e in moves2:
                if wiersz + e[0] < n and kol + e[1] >= 0 and wzg_pie(T[wiersz][kol], T[wiersz + e[0]][kol + e[1]]):
                    rek(ruchy + 1, wiersz + e[0], kol + e[1], 2)
            return ruchy2

    pierwsza = rek(0, 0, 0, 1)
    druga = rek(0, 0, 4, 2)
    print(pierwsza, druga)
    if pierwsza > druga:
        print("wygrywa pierwsza")
    elif druga > pierwsza:
        print("wygrywa druga")
    else:
        print("wynik nierozstrzygnięty")


zad3(T)
