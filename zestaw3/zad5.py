# Zadanie 5.
# Napisać program, który wczytuje wprowadzany z klawiatury
# ciąg liczb naturalnych zakończonych zerem stanowiącym wyłącznie
# znacznik końca danych.
# Program powinien wypisać 10 co do wielkości wartość,
# jaka wystąpiła w ciągu.
# Można założyć, że w ciągu znajduje się wystarczająca liczba elementów.

def algorytm():
    a = int(input())
    tab = []
    while a != 0:
        tab.append(a)
        a = int(input())
    tab = sorted(tab)
    return tab[-10]


print(algorytm())
