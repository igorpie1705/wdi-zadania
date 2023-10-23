# Zadanie 8.
# Dana jest N-elementowa tablica t zawierająca liczby naturalne.
# W tablicy możemy przeskoczyć z pola o indeksie k o n pól w prawo
# jeżeli wartość n jest czynnikiem pierwszym liczby t[k].
# Napisać funkcję sprawdzającą czy jest możliwe przejście
# z pierwszego pola tablicy na ostatnie pole.

t = [4, 3, 6, 1, 9, 5, 3, 6, 13, 35]

def algorytm(tab):
    for n in range(len(tab)-1):
        pass