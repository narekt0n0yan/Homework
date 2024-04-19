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
        a = self.head
        var = 0
        if index == 0:
            self.head = new_node
        else:
            while a is not None and var < index - 1:
                var += 1
                a.
            a.next = new_node


l = SingleLinkedList(Node(3))
l.append(Node(5))
l.append(Node(6))
l.append(Node(11))
l.insert(Node(7), 2)
l.traverse()
