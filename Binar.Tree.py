class Node():
    def __init__(self, value):
        self.right = None
        self.left  = None
        self.value = value 





class BinarTree():
    def __init__(self, head):
        self.root = head
    
    def add(self, new_int: int) -> bool:
        current_node: Node = self.root
        while current_node is not None:
            if current_node.value > new_int:
                if current_node.left is None:
                    break
                else:
                    current_node = current_node.left
            elif current_node.value < new_int:
                if current_node.right is None:
                    break
                else:
                    current_node = current_node.right
            else:
                return False
        if new_int > current_node.value:
            current_node.right = Node(new_int)
        else:
            current_node.left = Node(new_int)
        return True
    
    
    def delete(self, value: int) -> bool:
        current_node: Node = self.root
        prev_node: Node = None
        if value == current_node.value:
            return False
        while current_node != value:
            if current_node.value > value:
                prev_node = current_node
                current_node = current_node.left
            elif current_node < value:
                prev_node = current_node
                current_node = current_node.right
        prev_node.left = current_node.right
        left = current_node.left
        current_node = current_node.right
        while current_node.left is not None:
            current_node = current_node.left
        current_node.left = left

        
        


l = BinarTree(Node(10))
l.add(6)
print(l)
        


