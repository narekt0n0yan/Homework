class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        

class SingleLinkedList():
    def __init__(self, head=None):
        self.head = head

    def traverse(self):
        a = self.head
        while a is not None:
            print(a.value)
            a = a.next

    def append(self, new_node):
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = new_node

    def insert(self, new_node, index):
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            a = self.head
            var = 0
            while a is not None and var < index - 1:
                var += 1
                a = a.next
            new_node.next = a.next
            a.next = new_node

    def __add__(self, other):
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = other.head
        return self

    def __repr__(self):
        a = self.head
        result = ''
        while a is not None:
            result += str(a.value) + ' '
            a = a.next
        return result






l = SingleLinkedList(Node(3))
l.append(Node(5))
l.append(Node(6))
l.append(Node(11))
l.insert(Node(7), 3)
print(l)

ol = SingleLinkedList(Node(1))
ol.append(Node(2))
ol.append(Node(3))
print(ol)
print(ol + l)
# print(ol.__add__(l))
