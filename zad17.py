# Zadanie 17. Proszę napisać program wyznaczający wartość
# do której zmierza iloraz dwóch kolejnych wyrazów ciągu Fibonacciego.
# Wyznaczyć ten iloraz dla różnych wartości początkowych wyrazów ciągu.

def gowno(a, b):
    iloraz = 0
    for i in range(100):
        iloraz = b / a
        a, b = b, a + b
    print(iloraz)

gowno(1234, 531432)
