# 32. Lista reprezentuje wielomian o współczynnikach całkowitych. Elementy w
# liście ułożone są według rosnących potęg. Proszę napisać funkcję
# obliczającą różnicę dwóch dowolnych wielomianów. Wielomiany reprezentowane
# są przez wyżej opisane listy. Procedura powinna zwracać wskaźnik do nowo
# utworzonej listy reprezentującej wielomian wynikowy. Listy wejściowe
# powinny pozostać niezmienione.

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


def funkcja(start1, start2):
    p = start1
    q = start2
    g = Node()
    start = g
    while p.next != None and q.next != None:
        g.next = Node(p.next.val + q.next.val)
        g = g.next
        p = p.next
        q = q.next
    g = start
    return g



a = Node(2)
b = Node(-3)
c = Node(5)
d = Node(8)
e = Node(-5)
d.next = e
c.next = d
b.next = c
a.next = b
v = Node(8)
w = Node(2)
x = Node(12)
y = Node(4)
v.next = w
w.next = x
x.next = y

g1 = Node()
g2 = Node()
g1.next = a
g2.next = v
print_list(g1)
print_list(g2)
print_list(funkcja(g1, g2))
