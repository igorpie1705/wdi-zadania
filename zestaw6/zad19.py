# Zadanie 19. Elementy w liście są uporządkowane według wartości klucza. Proszę napisać funkcję usuwającą z listy
# elementy o nieunikalnym kluczu. Do funkcji przekazujemy wskazanie na pierwszy element listy, funkcja powinna
# zwrócić liczbę usuniętych elementów.

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


def exterminate(p):
    cnt = 0
    unikalne = []
    while p.next != None:
        if p.next.val not in unikalne:
            unikalne += [p.next.val]
            p = p.next
        else:
            cnt += 1
            p.next = p.next.next
    return cnt

e = Node(1, None)
d = Node(5, e)
c = Node(5, d)
b = Node(2, c)
a = Node(1, b)
g = Node(None, a)
print_list(g)
print(exterminate(g))
print_list(g)
