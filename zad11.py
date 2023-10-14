# Zadanie 11
# Proszę napisać program wyszukujący liczby zaprzyjaźnione mniejsze od miliona.

def funkcja():
    for n in range(1, 1000001):
        suma_dzielnikow_pierwsza = 1
        suma_dzielnikow_druga = 1
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                suma_dzielnikow_pierwsza += i
                suma_dzielnikow_pierwsza += (n // i)
        if suma_dzielnikow_pierwsza > n:
            for m in range(2, int(suma_dzielnikow_pierwsza ** 0.5)+1):
                if suma_dzielnikow_pierwsza % m == 0:
                    suma_dzielnikow_druga += m
                    suma_dzielnikow_druga += (suma_dzielnikow_pierwsza // m)
        if suma_dzielnikow_druga == n:
            print(n, suma_dzielnikow_pierwsza)



funkcja()
