# Zadanie 16. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy jednokierunkowej,
# przenosi na początek listy te z nich, które mają parzystą ilość piątek w zapisie ósemkowym.

def funkcja(n):
    cnt = 0
    liczba = ''
    while n > 0:
        liczba += str(n % 8)
        n //= 8
    liczba = liczba[::-1]
    for i in liczba:
        if i == "5":
            cnt += 1
    if cnt % 2 == 0 and cnt != 0:
        return True
    return False


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


def przenies(p):
    start = p
    p = p.next
    while p.next != None:
        if funkcja(p.next.val):
            new = Node(p.next.val, start.next)
            start.next = new
            p.next = p.next.next
        else:
            p = p.next
    return start


e = Node(54, None)
d = Node(215, e)
c = Node(873, d)
b = Node(153, c)
a = Node(531, b)
g = Node(None, a)
print_list(g)
przenies(g)
print_list(g)
