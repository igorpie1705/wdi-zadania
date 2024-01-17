# Zadanie 15. Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy jednokierunkowej,
# usuwa z niej wszystkie elementy, w których wartość klucza w zapisie trójkowym ma większą ilość jedynek niż dwójek.

def ten_to_three(n):
    liczba = ''
    while n > 0:
        liczba += str(n % 3)
        n //= 3
    return int(liczba[::-1])

def wiecej(n):
    n = str(ten_to_three(n))
    cnt1 = 0
    cnt2 = 0
    for i in n:
        if i == "1":
            cnt1 += 1
        if i == "2":
            cnt2 += 1
    if cnt1 > cnt2:
        return True
    return False

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
    start = p
    while p.next != None:
        if wiecej(p.next.val):
            p.next = p.next.next
        p = p.next
    return start


d = Node(532)
c = Node(23, d)
b = Node(12, c)
a = Node(345, b)
g = Node(None, a)
print_list(g)
exterminate(g)
print_list(g)
