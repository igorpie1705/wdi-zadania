# Zadanie 8. Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi element listy. Do funkcji
# należy przekazać wskazanie na pierwszy element listy.

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def print_list(head):
    while head is not None:
        print(str(head.val) + ' -> ', end='')
        head = head.next
    print("KONIEC")


def frog_remove(start):
    p = start
    while p.next != None and p.next.next != None:
        p.next = p.next.next
        p = p.next
    return start


h = Node(8)
g = Node(7, h)
f = Node(6, g)
e = Node(5, f)
d = Node(4, e)
c = Node(3, d)
b = Node(2, c)
a = Node(1, b)
print_list(a)
frog_remove(a)
print_list(a)
