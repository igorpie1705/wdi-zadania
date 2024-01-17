
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def print_list(head):
    while head is not None:
        print(str(head.val) + ' -> ', end='')
        head = head.next
    print("KONIEC")


c = Node(3)
b = Node(2, c)
a = Node(1, b)

def reverse(p):
    if p.next == None:
        return p, p
    rev_start, rev_end = reverse(p.next)
    p.next = None
    rev_end.next = p
    return rev_start, p

print_list(reverse(a)[0])
