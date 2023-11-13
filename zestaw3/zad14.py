#
# Zadanie 14.
# Napisać program wyznaczający na drodze eksperymentu prawdopodobieństwo tego,
# że w grupie N przypadkowo spotkanych osób,
# co najmniej dwie urodziły się tego samego dnia roku.
# Wyznaczyć wartości prawdopodobieństwa dla N z zakresu 20-40.

def algorytm(n):
    if n >= 730:
        return 100
    return round((n/730) * 100, 2)


for i in range(20, 40):
    print(str(algorytm(i)) + "%")
