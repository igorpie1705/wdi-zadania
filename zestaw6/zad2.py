class Node:
    def __init__(self, val=None, index=None, next=None):
        self.val = val
        self.index = index
        self.next = next


def init():
    return Node()


def print_list(head):
    print("GUARDIAN" + " -> ", end="")
    while head.next is not None:
        print(str(head.next.val) + ' -> ', end='')
        head = head.next
    print("KONIEC")


def get(p, index):
    while p.next is not None:
        if p.next.index == index:
            return p.next.val
        elif p.next.index > index:
            break
        p = p.next
    return 0


def add(p, index, value):
    start = p
    while p.next is not None and p.next.index < index:
        p = p.next
    if p.next is not None and p.next.index == index:
        p.next.val = value
    else:
        new_node = Node(value, index, p.next)
        p.next = new_node
    return start


g = init()
g = add(g, 4, 4)
g = add(g, 2, 1)
print_list(g)