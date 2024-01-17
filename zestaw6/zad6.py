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


def add_element(p, to_add):
    start = p
    while p.next != None:
        p = p.next
    p.next = Node(to_add)
    return start


c = Node(3)
b = Node(2, c)
a = Node(1, b)
g = Node(None, a)
print_list(g)
a = add_element(g, 4)
print_list(g)