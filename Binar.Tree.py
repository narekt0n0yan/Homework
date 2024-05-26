class Node():
    def __init__(self, value):
        self.right = None
        self.left  = None
        self.value = value





class BinarTree():
    def __init__(self, head):
        self.root = head
    
    def add(self, new_int):
        a = self.root
        while a is not None:
            if new_int > a:
                a = self.left
            a = self.right
        if new_int > a:
            new_int = self.left
        new_int = self.right
            

l = BinarTree(Node(10))
# l.add(Node(6))
print(l)
        


