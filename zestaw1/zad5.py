# Zadanie 5
# Proszę napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona

def pierw(n):
    a = 1
    b = n
    while abs(a - b) > 0.000001:
        b = (a + b) / 2
        a = n / b
    return a


wynik = pierw(6)

print(wynik)

