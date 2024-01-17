# Zadanie 29. Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby naturalne. W obu listach
# liczby są posortowane rosnąco. Proszę napisać funkcję usuwającą z każdej listy liczby niewystępujące w
# drugiej. Do funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić łączną liczbę usuniętych
# elementów.


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


def funkcja(start1, start2):
    p = start1
    q = start2
    pierw = []
    drug = []
    while p.next != None:
        pierw += [p.next.val]
        p = p.next
    while q.next != None:
        drug += [q.next.val]
        q = q.next
    p = start1
    q = start2
    while p.next != None:
        if p.next.val not in drug:
            p.next = p.next.next
        else:
            p = p.next
    while q.next != None:
        if q.next.val not in pierw:
            q.next = q.next.next
        else:
            q = q.next
    return start1, start2


a = Node(1)
b = Node(68)
c = Node(9)
d = Node(14)
e = Node(25)


d.next = e
c.next = d
b.next = c
a.next = b


v = Node(3)
w = Node(9)
x = Node(8)
y = Node(1)
z = Node(68)
v.next = w
w.next = x
x.next = y
y.next = z


g1 = Node(None, a)
g2 = Node(None, v)
print_list(g1)
print_list(g2)
funkcja(g1, g2)
print_list(g1)
print_list(g2)
