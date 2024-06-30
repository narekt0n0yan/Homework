class Node():
    def __init__(self, value:int):
        self.right = None
        self.left  = None
        self.value = value

    def __repr__(self) -> str:
        return str(self.value)





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
        is_left = False
        while current_node.value != value:
            if current_node.value > value:
                prev_node = current_node
                current_node = current_node.left
                is_left = True
            if current_node.value < value:           
                prev_node = current_node
                current_node = current_node.right
                is_left = False

        print('HERE I AM', current_node, current_node.left, current_node.right, prev_node)
        if current_node.left is None:
            if  is_left:
                prev_node.left = current_node.right
                return  
            else:
                prev_node.right = current_node.right
                return    


        if current_node.right is None:
            if is_left:
                prev_node.left = current_node.left
                return
            else:
                prev_node.right = current_node.left


        prev_node.left = current_node.left
        temp = current_node.left
        while temp.right is not None:
            temp = temp.right
        temp.right = current_node.right
        


        
              
    def BedFind(self, value : int) -> bool:
        is_find = False
        def rec_find(current:Node):
           nonlocal is_find
           if is_find:
               return 
           if current.value == value:
               is_find = True
               return 
           if current.left is not None:
               rec_find(current.left)
           if current.right is not None:
               rec_find(current.right)
        rec_find(self.root)
        return is_find


    def GoodFind(self, value:int) -> bool:
        current = self.root
        while current.left is not None and current.right is not None:
            if current.value > value:
                current = current.left
            elif current.value < value:
                current = current.right
            else:
                return True
        return False
           

        
    
        
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
l.add(27)
l.add(99)
traverse(l.root)
#print(l.BedFind(8))
#print(l.GoodFind(11))
l.delete(23)
print('')
traverse(l.root)



        


