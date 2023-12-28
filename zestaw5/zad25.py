# Zadanie 23. Dana jest tablica T[N] zawierająca oporności N rezystorów wyrażonych całkowitą liczbą
# kΩ. Proszę napisać funkcję, która sprawdza czy jest możliwe uzyskanie wypadkowej rezystancji R (równej
# całkowitej liczbie kΩ) łącząc dowolnie 3 wybrane rezystory

T = [100, 330, 1000, 20, 40, 10, 250, 385, 210, 340, 500]


def zad23(t, k):
    n = len(t)

    def rek(i, suma, c):
        if c == 3 or i == n:
            if suma == k:
                return True
            return False

        return rek(i + 1, suma, c) or rek(i + 1, suma + t[i], c + 1)
    return rek(0, 0, 0)


print(zad23(T, 1840))
