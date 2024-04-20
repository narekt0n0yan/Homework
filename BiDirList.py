class BiNode():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class BiDirList():
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = new_node
        new_node.prev = a

    def insert(self, index, new_node):
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            a = self.head
            var = 0
            while a is not None and var < index - 1:
                a = a.next
                var += 1
            new_node.next = a.next
            a.next.prev = new_node
            new_node.prev = a
            a.next = new_node

    def __repr__(self):
        a = self.head
        result = ''
        while a is not None:
            result += str(a.value) + ' '
            a = a.next
        return result

l = BiDirList(BiNode(1))
l.append(BiNode(2))
l.append(BiNode(3))
l.append(BiNode(4))
l.append(BiNode(5))
l.append(BiNode(6))
print(l)
