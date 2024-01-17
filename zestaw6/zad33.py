# 33. Napis s1 poprzedza napis s2 jeżeli ostatnia litera s1 jest „mniejsza”
# od pierwszej litery s2. Według tej zasady rozmieszczono napisy w liście
# cyklicznej, na przykład:
# ┌─bartek──leszek──marek──ola──zosia─┐
# └───────────────────────────────────┘
# Proszę napisać stosowne definicje typów oraz funkcję wstawiającą do listy
# napis z zachowaniem zasady poprzedzania. Do funkcji należy przekazać
# wskaźnik do listy oraz wstawiany napis, funkcja powinna zwrócić wartość
# logiczną wskazującą, czy udało się wstawić napis do listy. Po wstawieniu
# elementu wskaźnik do listy powinien wskazywać na nowo wstawiony element.

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def print_list(head):
    print("GUARDIAN" + " -> ", end="")
    while head.next is not None:
        print(str(head.next.val) + ' -> ', end='')
        head = head.next
    print("KONIEC")

def funkcja(p, napis):
    start = p
    f = napis[0]
    l = napis[-1]
    while p.next != start:
        w1 = p.val[-1]
        w2 = p.next.val[0]
        if w1 < f and w2 > l:
            new = Node(napis)
            new.next = p.next
            p.next = new
            return True
        p = p.next
    return False


a = Node("bartek")
b = Node("leszek")
c = Node("marek")
d = Node("ola")
e = Node("zosia")

e.next = a
d.next = e
c.next = d
b.next = c
a.next = b

print(funkcja(a, "chujpizdakurwaz"))