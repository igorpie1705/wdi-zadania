# Zadanie 3.
# Proszę napisać program wczytujący liczbę naturalną
# i odpowiadający na pytanie,
# czy liczba naturalna jest palindromem,
# a następnie czy jest palindromem w systemie dwójkowym.

# 4554

def czy_palindrom(n):
    d = str(bin(n)[2::])
    print(n, d)
    n = str(n)
    for i in range(1, len(n)//2):
        if n[i] != n[len(n)-1-i]:
            print("NIE")
            return 0
    for i in range(1, len(d)//2):
        if d[i] != d[len(d)-1-i]:
            print("NIE")
            return 0
    print("TAK")


czy_palindrom(15351)
