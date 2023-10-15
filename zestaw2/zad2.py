# Zadanie 2.
# Proszę napisać program wczytujący
# trzy liczby naturalne a, b, n i wypisujący rozwinięcie
# dziesiętne ułamka a/b z dokładnością
# do n miejsc po kropce dziesiętnej. (n jest rzędu 100)

def algorytm(a, b, n):
    return round(a / b, n)


print(algorytm(5, 23, 9))
