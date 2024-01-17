# 34. Proszę napisać funkcję, która usuwa z listy cyklicznej elementy,
# których klucz występuje dokładnie k razy. Do funkcji należy przekazać
# wskazanie na jeden z elementów listy, oraz liczbę k, funkcja powinna
# zwrócić informację czy usunięto jakieś elementy z listy.


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def print_list(head):
    print("GUARDIAN" + " -> ", end="")
    for i in range(10):
        print(str(head.next.val) + ' -> ', end='')
        head = head.next
    print("KONIEC")


def funkcja(start, k):
    p = start.next
    lista = []
    while p.next != start.next:
        if p.next.val not in lista:
            lista += [p.next.val]
        p = p.next
    to_del = []
    for x in lista:
        cnt = 0
        p = start.next
        if p == start.next and p.val == x:
            cnt += 1
        while p.next != start.next:
            if p.next.val == x:
                cnt += 1
            p = p.next
        if cnt == k:
            to_del += [x]
    print(to_del)
    p = start
    while p.next.val in to_del:
        p.next = p.next.next
    else:
        p = p.next

    while p.next != start.next:
        if p.next.val in to_del:
            p.next = p.next.next
        else:
            p = p.next
    print_list(start)


a = Node(1)
b = Node(9)
c = Node(8)
d = Node(8)
e = Node(8)

e.next = a
d.next = e
c.next = d
b.next = c
a.next = b
g = Node()
g.next = a


funkcja(g, 3)
print("wreszcie dziala kurwa")