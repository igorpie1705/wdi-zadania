# Zadanie 22. Dana jestlista, który być może zakończona jest cyklem. Napisać funkcję, która sprawdza ten fakt.

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
    while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False


a = Node(1)
e = Node(1)
d = Node(5, e)
c = Node(5, d)
b = Node(2, c)
a.next = b
g = Node(None, a)
print(czy_cykl(g))