# Zadanie 7. Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji należy przekazać wskazanie
# na pierwszy element listy.

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


def remove_element(p):
    start = p
    if p.next == None:
        return start
    while p.next.next != None:
        p = p.next
    p.next = p.next.next
    return start


c = Node(3)
b = Node(2, c)
a = Node(1, b)
g = Node(None, a)
print_list(g)
a = remove_element(g)
print_list(g)
