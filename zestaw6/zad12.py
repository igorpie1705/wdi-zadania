# Zadanie 12. Zbiór mnogościowy zawierający napisy jest reprezentowany w postaci jednokierunkowej listy.
# Napisy w łańcuchu są uporządkowane leksykograficznie. Proszę napisać stosowne definicje typów oraz funkcję
# dodającą napis do zbioru. Do funkcji należy przekazać wskaźnik do listy oraz wstawiany napis, funkcja
# powinna zwrócić wartość logiczną wskazującą, czy w wyniku operacji moc zbioru uległa zmianie.

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


def dodaj_napis(p, napis):
    start = p
    while p.next != None:
        if napis < p.next.val:
            new = Node(napis, p.next)
            p.next = new
            return start
        p = p.next
    p.next = Node(napis)
    return start


d = Node("eaniel")
c = Node("decylia", d)
b = Node("basia", c)
a = Node("barek", b)
g = Node(None, a)
print_list(g)
dodaj_napis(g, "chuj")
print_list(g)
