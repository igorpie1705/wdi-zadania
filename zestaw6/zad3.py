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


z = Node(6)
y = Node(5, z)
x = Node(4, y)
w = Node(None, x)

c = Node(3)
b = Node(2, c)
a = Node(1, b)
g = Node(None, a)


def scal(p, q):
    start = p
    while p.next != None:
        p = p.next
    p.next = q.next
    return start


print_list(scal(g, w))
