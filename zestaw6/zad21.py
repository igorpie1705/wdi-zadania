# Zadanie 21. Kolejne elementy listy o zwiększającej się wartości pola val nazywamy podlistą rosnącą.
# Proszę napisać funkcję, która usuwa z listy wejściowej najdłuższą podlistę rosnącą. Warunkiem usunięcia
# jest istnienie w liście dokładnie jednej najdłuższej podlisty rosnącej.

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def funkcja(start):
    p = start
    max_dl = 0
    while p.next != None and p.next.next != None:
        if p.next.next.val > p.next.val:
            cnt = 1
            while p.next != None and p.next.next != None and p.next.next.val > p.next.val:
                cnt += 1
                p = p.next
            if cnt > max_dl:
                max_dl = cnt
        p = p.next
    p = start
    while p.next != None and p.next.next != None:
        if p.next.next.val > p.next.val:
            zaczep = p
            cnt = 1
            while p.next != None and p.next.next != None and p.next.next.val > p.next.val:
                cnt += 1
                p = p.next

            if cnt == max_dl:
                zaczep.next = p.next.next
        p = p.next
    return start







def print_list(head):
    print("GUARDIAN" + " -> ", end="")
    while head.next is not None:
        print(str(head.next.val) + ' -> ', end='')
        head = head.next
    print("KONIEC")


a = Node(2)
b = Node(10)
c = Node(12)
d = Node(8)
e = Node(4)
f = Node(8)

e.next = f
d.next = e
c.next = d
b.next = c
a.next = b

g = Node(None, a)
print_list(g)
funkcja(g)
print_list(g)
