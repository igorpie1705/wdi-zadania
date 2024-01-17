# Zadanie 25. Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca wskaźnik do
# ostatniego elementu przed cyklem.

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

def czy_cykl(p):
    fast = p
    slow = p
    cnt = 0
    while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break
    slow = p
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next
    return slow.val

a = Node(1)
c = Node(5)
b = Node(1)
e = Node(25)
d = Node(10)

e.next = d
d.next = e
c.next = d
b.next = c
a.next = b

g = Node(None, a)

print(czy_cykl(g))
print("git")