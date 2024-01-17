# Zadanie 14. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy element listy o
# wartościach typu int, usuwającą wszystkie elementy, których wartość dzieli bez reszty wartość bezpośrednio
# następujących po nich elementów.

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


def exterminate(p):
    start = p
    while p.next != None and p.next.next != None:
        if p.next.val % p.next.next.val == 0:
            p.next = p.next.next
        p = p.next
    return start


e = Node(2)
d = Node(32, e)
c = Node(4, d)
b = Node(3, c)
a = Node(6, b)
g = Node(None, a)
print_list(g)
exterminate(g)
print_list(g)