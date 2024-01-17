# Zadanie 9. Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne elementy listy przechowują
# kolejne cyfry. Proszę napisać funkcję zwiększającą taką liczbę o 1.
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


def dodaj(p):
    start = p
    while p.next.next != None:
        p = p.next
    p.next.val += 1
    p = start
    print(p.next.val)

    while p.next != None:
        if p.next.val == 10:
            p.val += 1
            p.next.val = 0
        p = p.next
    return start


c = Node(9)
b = Node(9, c)
a = Node(8, b)
g = Node(None, a)
print_list(g)
dodaj(g)
print_list(g)
