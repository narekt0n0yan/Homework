
b = [[1,2,2],
     [1,7,4],
     [1,6,6],
     [2,7,10],
     [2,3,8],
     [7,6,12],
     [7,4,20],
     [6,5,14],
     [3,4,16],
     [4,5,18],
    ]

a = [
    [0,1,1],
    [1,2,3],
    [2,3,3],
    [3,4,4],
    [4,5,6],
    [5,6,12],
    [6,7,3],
    [7,8,6],
    [8,9,7],
    [9,0,8],
    [9,10,3],
    [10,1,1],
    [10,2,1],
    [10,11,20],
    [10,7,5],
    [11,2,3],
    [11,12,7],
    [12,3,4],
    [12,5,8],
    [12,6,4],
    [12,7,1],
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

    def nodeset(self) -> set:
        NodesSet = set()
        for i in self.graph[:-1:]:
            for j in i[:-1:]:
                NodesSet.add(j)
        return NodesSet


    def nodewhitneighbor(self) -> dict:
        NodesList = self.nodeset()
                
        myDict = {}

        myDict = {x: [] for x in NodesList}
        for tox in self.graph:
                myDict[tox[0]].append(tox[1])
                myDict[tox[1]].append(tox[0])
        return myDict
    
    def neighborwhitway(self) -> dict:

        myDict = {}
        for i in self.graph:
            myDict[(i[0],i[1])] = i[2]
            myDict[(i[1],i[0])] = i[2]
        return myDict
    
    def shortestpath(self,start,finish):
        TempNodeList = self.nodeset()
        Nodeslist = list(self.nodeset()) 
        TempNodewithNeighbour = self.nodewhitneighbor()

        temp = start
    
        pathdict = {}
        pathdict = {x:float('inf') for x in Nodeslist}
        pathdict[temp] = 0 
        
        outlist = set()

        firststep = []

        for i in TempNodewithNeighbour[temp]:
            if pathdict[i] > pathdict[temp] + self.neighborwhitway()[temp,i]:
                pathdict[i] = pathdict[temp] +self.neighborwhitway()[temp,i]
                firststep.append(i)

        outlist.add(temp)
        current = float('inf')
        for f in firststep:
            if pathdict[f] < current:
                current = f
        print(current)
        while TempNodeList != outlist:
            if current == float('inf'):
                break
            currentlist = []
            for j in TempNodewithNeighbour[current]:
                if j not in outlist:
                    currentlist.append(j)
                outlist.add(current)
                if j not in outlist and pathdict[j] > pathdict[current] + self.neighborwhitway()[current,j]:
                    pathdict[j] = pathdict[current] + self.neighborwhitway()[current,j]
           
            current = float('inf')
            
            for k in currentlist:
                if pathdict[k] < current:
                    current = k
            print(outlist)
            print(TempNodeList)
        
        print(pathdict[finish])
    

                
                    

                
new_graph = Graph(a)
# new_graph.add(10,15,20)
# new_graph.traverse()
# print(new_graph.find(1))
# print(new_graph.find(1100))
# print(new_graph.nodewhitneighbor())
# print('====================')
# print(new_graph.neighborwhitway())
# print('=====================')
new_graph.shortestpath(1,9)
# new_graph.nodeset()