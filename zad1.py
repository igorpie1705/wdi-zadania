# Zadanie 1. Proszę napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona.

def ciag_fibonacciego():
    a, b = 0, 1
    while b < 1000000:
        print(b, end=" ")
        a, b = b, a + b
    return 0


ciag_fibonacciego()
