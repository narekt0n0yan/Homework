class Node():
    def __init__(self, value:int):
        self.right = None
        self.left  = None
        self.value = value 





class BinarTree():
    def __init__(self, head: Node):
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
        while current_node.value != value:
            if current_node.value > value:
                prev_node = current_node
                current_node = current_node.left
            elif current_node.value < value:
                prev_node = current_node
                current_node = current_node.right
        prev_node.left = current_node.right
        left = current_node.left
        current_node = current_node.right
        while current_node.left is not None:
            current_node = current_node.left
        current_node.left = left



        



    def find(self, value : int) -> bool:
        def rec_find(current:Node):
            if current.left is None and current.right is None:
                if current.value == value:
                    print('True')
            if current.left is not None:
                rec_find(current.left)
                if current.value == value:
                    print('True')
            if current.right is not None:
                if current.value == value:
                    print('True')
                rec_find(current.right)
        rec_find(self.root)
                    


    
        
def traverse(current:  Node):
    if current.left is None and current.right is None:     
        print(current.value, end=', ')
        return
    is_printed = False
    if current.left is not None:
        traverse(current.left)
        print(current.value, end=', ')
        is_printed = True
    if current.right is not None:
        if not is_printed:
            print(current.value, end=', ')
        traverse(current.right)

       
    
            
            






l = BinarTree(Node(16))
l.add(11)
l.add(13)
l.add(12)
l.add(14)
l.add(15)
l.add(8)
l.add(2)
l.add(21)
l.add(23)
l.add(17)
l.add(18)
l.add(19)
l.add(27)
l.add(99)
traverse(l.root)
l.find(800)

#l.delete(11)




        


