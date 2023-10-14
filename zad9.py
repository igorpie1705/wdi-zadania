# Zadanie 9
# Proszę napisać program wypisujący podzielniki liczby.

def podzielniki(n):
    tab = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            tab.append(i)
            tab.append(n//i)
            n //= i
    if len(tab) == 0:
        tab = [1, n]
    return tab


print(podzielniki(234325))


