class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def print_list(head):
    while head is not None:
        print(str(head.val) + ' -> ', end='')
        head = head.next
    print("KONIEC")


def add_element(p, to_add):
    start = p
    prev = None
    while prev is not None:
        prev = p
        p = p.next
    if prev is None:
        return Node(to_add)
    prev.next = Node(to_add)
    return start


def remove_element(p, to_delete):
    prev = None
    start = p

    while p is not None:
        if p.val == to_delete:
            if prev is None:
                return p.next
            else:
                prev.next = prev.next.next
                return start
        prev = p
        p = p.next
    return start


c = Node(3)
b = Node(2, c)
a = Node(1, b)

a = remove_element(a, 2)

print_list(a)
