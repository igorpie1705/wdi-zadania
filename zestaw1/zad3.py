# Zadanie 3. Proszę napisać program sprawdzający,
# czy istnieje spójny podciąg ciągu Fibonacciego o zadanej sumie.

def funkcja(suma):
    a, b = 0, 1
    tab = [a, b]
    while b <= suma:
        a, b = b, a + b
        tab.append(b)
        for i in range(0, len(tab)):
            nowa_suma = 0
            for j in range(i, len(tab)):
                nowa_suma += tab[j]
                if nowa_suma == suma:
                    print("TAK")
                    return 0
    print("NIE")


dane = int(input("Podaj sumę: "))
funkcja(dane)
