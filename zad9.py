# Zadanie 9
# Proszę napisać program wypisujący podzielniki liczby.

def podzielniki(n):
    tab = []
    for i in range(2, n):
        while n % i == 0:
            tab.append(i)
            n //= i
    if len(tab) == 0:
        tab = [1, n]
    return tab


print(podzielniki(32489423))


