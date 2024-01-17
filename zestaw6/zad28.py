# Zadanie 28. Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby naturalne. W pierwszej liście
# liczby są posortowane rosnąco, a w drugiej nie. Proszę napisać funkcję usuwającą z obu list liczby występujące
# w obu listach. Do funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić łączną liczbę
# usuniętych elementów.


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


def funkcja(p, q):
    lista = []
    unique = []
    start1 = p
    while p.next != None:
        if p.next.val not in lista:
            lista += [p.next.val]
        p = p.next
    p = start1
    start2 = q
    while q.next != None:
        if q.next.val in lista:
            unique += [q.next.val]
        q = q.next
    q = start2
    while p.next != None:
        if p.next.val in unique:
            p.next = p.next.next
        else:
            p = p.next
    while q.next != None:
        if q.next.val in unique:
            q.next = q.next.next
        else:
            q = q.next
    return start1, start2



a = Node(1)
b = Node(5)
c = Node(9)
d = Node(10)
e = Node(25)


d.next = e
c.next = d
b.next = c
a.next = b


v = Node(3)
w = Node(2)
x = Node(25)
y = Node(1)
z = Node(34)
v.next = w
w.next = x
x.next = y
y.next = z


g1 = Node(None, a)
g2 = Node(None, v)
print_list(g1)
print_list(g2)
g1 = funkcja(g1, g2)
print_list(g1[0])
print_list(g1[1])
