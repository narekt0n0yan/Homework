


a = [
    [1, 2, 10],
    [2, 3, 20],
    [1, 3, 4],
    [4, 5, -6]
    ]


class Graph():
    def __init__(self, graph:list) -> None:
        self.graph = graph

    def add(self, value: int, neighbour: int, weight: int) -> None:
        NewGraph = [value, neighbour, weight]
        self.graph.append(NewGraph)
        return self.graph
        
    
    def find(self, value) -> bool:
        for i in self.graph:
            if i[0] == value:
                return True
        return False
            
    
    def traverse(self) -> str:
        for i in self.graph:
            print(i)



new_graph = Graph(a)
new_graph.add(10,15,20)
new_graph.traverse()
print(new_graph.find(1))
print(new_graph.find(1100))