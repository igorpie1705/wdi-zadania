# Zadanie 2.
# Napisać funkcje sprawdzającą, czy dwie liczby
# naturalnesą one zbudowane z takich samych
# cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001.

def algorytm(a, b):
    str_a = sorted(str(a))
    str_b = sorted(str(b))
    if str_a == str_b:
        print("TAK")
    else:
        print("NIE")


algorytm(11000, 10001)
