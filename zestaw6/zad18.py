# Zadanie 18. Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy unikalne. Do funkcji
# należy przekazać wskazanie na pierwszy element listy

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


