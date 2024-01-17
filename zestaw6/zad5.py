# Zadanie 5. Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do 10 list, według ostatniej cyfry
# pola val. W drugim kroku powstałe listy należy połączyć w jedną listę odsyłaczową, która jest posortowana
# niemalejąco według ostatniej cyfry pola val.


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


f = Node(1)
e = Node(8, f)
d = Node(6, e)
c = Node(3, d)
b = Node(5, c)
a = Node(2, b)
g = Node(None, a)


def sortuj(p):
    start = p
    lista = []
    while p.next != None:
        lista += [p.next.val]
        p = p.next
    p = start
    while len(lista) > 0:
        while p.next != None:
            p.next.val = max(lista)
            lista.remove(max(lista))
            p = p.next
    return start

print_list(g)
print_list(sortuj(g))
print("chyba zle")