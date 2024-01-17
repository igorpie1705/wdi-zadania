# Zadanie 30. Dane są dwie niepuste listy, z których każda zawiera niepowtarzające się elementy. Elementy
# w pierwszej liście są uporządkowane rosnąco, w drugiej elementy występują w przypadkowej kolejności.
# Proszę napisać funkcję, która z dwóch takich list stworzy jedną, w której uporządkowane elementy będą
# stanowić sumę mnogościową elementów z list wejściowych. Do funkcji należy przekazać wskazania na obie
# listy, funkcja powinna zwrócić wskazanie na listę wynikową. Na przykład dla list:
# 2 -> 3 -> 5 -> 7-> 11 oraz 8 -> 2 -> 7 -> 4 powinna pozostać lista: 2 -> 3 -> 4 -> 5 -> 7 -> 8 -> 11

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
    lista = []
    while p.next != None:
        lista += [p.next.val]
        p = p.next
    lista2 = []
    while q.next != None:
        if q.next.val not in lista:
            lista2 += [q.next.val]
        q = q.next
    for element in lista2:
        p = start1
        while p.next != None:
            if element < p.next.val:
                new = Node(element)
                new.next = p.next
                p.next = new
                break
            p = p.next
        if p.next == None:
            p.next = Node(element)
    return start1






a = Node(2)
b = Node(3)
c = Node(5)
d = Node(7)
e = Node(11)
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
funkcja(g1, g2)
print_list(g1)
