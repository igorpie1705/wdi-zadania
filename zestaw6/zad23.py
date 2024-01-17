# Zadanie 23. Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca liczbę elementów
# w cyklu.

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
    cnt = 1
    while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break
    slow = slow.next
    while slow != fast:
        slow = slow.next
        cnt += 1
    return cnt


a = Node(1)
c = Node(5)
e = Node(25, c)
d = Node(10, e)
b = Node(1, c)
c.next = d
a.next = b
g = Node(None, a)
print(czy_cykl(g))