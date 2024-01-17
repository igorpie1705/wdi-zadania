class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next



def print_list(head):
    print("GUARDIAN" + " -> ", end="")
    while head.next != None:
        print(str(head.next.val) + " -> ", end="")
        head = head.next
    print("KONIEC")


def add_element(p, to_add):
    start = p
    while p.next != None:
        p = p.next
    p.next = Node(to_add)
    return start

def remove_element(p, to_remove):
    start = p
    while p.next != None:
        if p.next.val == to_remove:
            p.next = p.next.next
            return start
        p = p.next
    return start

def czy_nalezy(p, element):
    start = p
    while p.next != None:
        if p.next.val == element:
            return True
        p = p.next
    return False

c = Node(3)
b = Node(2, c)
a = Node(1, b)
g = Node(None, a)
a = add_element(g, 4)
a = remove_element(g, 2)
print_list(g)
print(czy_nalezy(g, 3))