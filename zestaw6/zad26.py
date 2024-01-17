# Zadanie 26. Proszę napisać funkcję, która sprawdza, czy jedna lista zawiera się w drugiej. Do funkcji należy
# przekazać wskazania na pierwsze elementy obu list, funkcja powinna zwrócić wartość logiczną

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

def sprawdz(p, q):
    start1 = p
    start2 = q
    while p.next != None:
        if p.next.val == q.next.val:
            start2 = p
            while q.next != None and p.next != None:
                p = p.next
                q = q.next
                if p.val != q.val:
                    break
            if q.next == None and q.val == p.val:
                return True
            else:
                q = start2
                p = start1.next
        p = p.next
    return False


a = Node(2)
b = Node(5)
c = Node(9)

b.next = c
a.next = b


v = Node(2)
w = Node(5)
x = Node(9)
y = Node(1)
z = Node(2)
v.next = w
w.next = x
x.next = y
y.next = z


g1 = Node(None)
g2 = Node(None)
g1.next = a
g2.next = v
print_list(g1)
print(sprawdz(g2, g1))
print_list(g2)
