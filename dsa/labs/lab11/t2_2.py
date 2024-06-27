class GraphNode:
    def __init__(self, vertex=0, next_node=None):
        self.vertex = vertex
        self.next = next_node

class Graph:
    def __init__(self, mx):
        self.MAX = mx
        self.headnodes = [None] * self.MAX

    def addEdge(self, vertex1, vertex2):
        newNode = GraphNode(vertex2, self.headnodes[vertex1])
        self.headnodes[vertex1] = newNode

    def printGraph(self):
        for i in range(self.MAX):
            print(f"{i} ->", end=" ")
            curr = self.headnodes[i]
            if curr is None:
                print("x", end="")
            while curr is not None:
                print(f" {curr.vertex}", end=" ")
                curr = curr.next
            print()

def directedGraph():
    # mx = int(input("Enter the number of vertices: "))
    ug = Graph(5)
    # n = int(input("Enter the number of edges: "))
    
    # for _ in range(n):
    #     v1, v2 = map(int, input().split())
    #     ug.addEdge(v1, v2)
    
    ug.addEdge(1,2)
    ug.addEdge(2,3)
    ug.addEdge(1,4)
    ug.addEdge(1,5)
    ug.addEdge(4,5)

    ug.printGraph()


directedGraph()
