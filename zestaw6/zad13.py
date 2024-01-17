# Zadanie 13. Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy element listy o
# wartościach typu int, usuwającą wszystkie elementy, których wartość jest mniejsza od wartości bezpośrednio
# poprzedzających je elementów.

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
    p = p.next
    while p.next != None:
        if p.next.val < p.val:
            p.next = p.next.next
            if p.next == None:
                return start
        p = p.next
    return start



e = Node(32)
d = Node(52, e)
c = Node(4, d)
b = Node(6, c)
a = Node(5, b)
g = Node(None, a)
print_list(g)
exterminate(g)
print_list(g)
