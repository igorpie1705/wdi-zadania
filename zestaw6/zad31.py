# Zadanie 31. Proszę napisać funkcję, która rozdziela listę na dwie listy. Pierwsza powinna zawierać klucze
# parzyste dodatnie, drugi klucze nieparzyste ujemne, pozostałe elementy należy usunąć z pamięci. Do funkcji
# należy przekazać wskaźniki na listę z danymi oraz wskaźniki na listy wynikowe. Funkcja powinna zwrócić
# liczbę usuniętych elementów.

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


def funkcja(start1, kon1, kon2):
    p = start1
    a = kon1
    b = kon2
    s1 = 0
    s2 = 0
    cnt = 0
    while p.next != None:
        cnt += 1
        if p.next.val > 0 and p.next.val % 2 == 0:
            a.next = Node(p.next.val)
            a = a.next
            s1 += 1
        if p.next.val < 0 and p.next.val % 2 == 1:
            b.next = Node(p.next.val)
            b = b.next
            s2 += 1
        p = p.next
    print_list(kon1)
    print_list(kon2)
    return cnt - s1 - s2




a = Node(2)
b = Node(-3)
c = Node(5)
d = Node(8)
e = Node(-5)
d.next = e
c.next = d
b.next = c
a.next = b


g = Node()
g.next = a
print_list(g)
g1 = Node()
g2 = Node()
print(funkcja(g, g1, g2))
print("ezzzz")

