# Zadanie 11. Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do której przekazujemy
# wskaźnik na początek oraz wartość klucza. Jeżeli element o takim kluczu występuje w liście należy go usunąć
# z listy. Jeżeli elementu o zadanym kluczu brak w liście należy element o takim kluczu wstawić do listy.

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


def usun_element(p, to_remove):
    start = p
    while p.next != None:
        if p.next.val == to_remove:
            p.next = p.next.next
            return start
        p = p.next
    p.next = Node(to_remove)
    return start





f = Node(6)
e = Node(5, f)
d = Node(4, e)
c = Node(3, d)
b = Node(2, c)
a = Node(1, b)
g = Node(None, a)
usun_element(g, 89)

print_list(g)