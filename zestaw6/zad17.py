# Zadanie 17. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy dwukierunkowej,
# usuwa z niej wszystkie elementy, w których wartość klucza w zapisie binarnym ma nieparzystą ilość jedynek.


class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def print_list(head):
    print("GUARDIAN" + " -> ", end="")
    while head.next is not None:
        print(str(head.next.val) + ' -> ', end='')
        head = head.next
    print("KONIEC")


def dec_to_bin(n):
    cnt = 0
    liczba = ''
    while n > 0:
        liczba += str(n % 2)
        n //= 2
    liczba = liczba[::-1]
    for i in liczba:
        if i == "1":
            cnt += 1
    if cnt % 2 == 1:
        return True
    return False


def exterminate(p):
    start = p
    while p.next != None:
        if dec_to_bin(p.next.val):
            p.next = p.next.next
        else:
            p = p.next
    return start


e = Node(512, None)
d = Node(2124, e)
c = Node(423, d)
b = Node(32, c)
a = Node(512, b)
g = Node(None, a)
print_list(g)
exterminate(g)
print_list(g)
