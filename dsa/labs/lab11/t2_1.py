from collections import deque

class GraphNode:
    def __init__(self, vertex=0, next_node=None):
        self.vertex = vertex  # Vertex identifier
        self.next = next_node

class Graph:
    def __init__(self, mx):
        self.MAX = mx
        self.headnodes = [None] * self.MAX  
        self.visited = [False] * self.MAX  

    def initialize_visited(self):
        self.visited = [False] * self.MAX

    def addVertex(self, vertex):
        if vertex < self.MAX:
            self.headnodes[vertex] = GraphNode(vertex)
        else:
            print('Vertex out of bounds')

    def removeVertex(self, vertex):
        if vertex < self.MAX:
            for node in self.headnodes:
                temp = node
                while temp:
                    if temp.next and temp.next.vertex == vertex:
                        temp.next = temp.next.next
                        break 
                    temp = temp.next
            self.headnodes[vertex] = None
            print(f'Removed vertex {vertex} from graph')
        else:
            print('Vertex out of bounds')

    def addEdge(self, vertex1, vertex2):
        if vertex1 < self.MAX and vertex2 < self.MAX:
            newNode = GraphNode(vertex2, self.headnodes[vertex1].next)
            self.headnodes[vertex1].next = newNode

    def removeEdge(self, vertex1, vertex2):
        if vertex1 < self.MAX and vertex2 < self.MAX:
            temp = self.headnodes[vertex1]
            while temp:
                if temp.next and temp.next.vertex == vertex2:
                    temp.next = temp.next.next
                    break
                temp = temp.next

            temp = self.headnodes[vertex2]
            while temp:
                if temp.next and temp.next.vertex == vertex1:
                    temp.next = temp.next.next
                    break
                temp = temp.next

    def vertexExists(self, vertex):
        return vertex < self.MAX and self.headnodes[vertex] is not None

    def printGraph(self):
        for i in range(self.MAX):
            if self.headnodes[i] is not None:
                print(f"{i} ->", end=" ")
                curr = self.headnodes[i].next
                if curr is None:
                    print("x", end="")
                while curr is not None:
                    print(f"{curr.vertex}", end=" ")
                    curr = curr.next
                print()
            else:
                print(f"{i} -> x")

    def dfs(self, vertex):
        def dfsHelper(v):
            self.visited[v] = True
            print(v, end=' ')

            temp = self.headnodes[v].next
            while temp:
                if not self.visited[temp.vertex]:
                    dfsHelper(temp.vertex)
                temp = temp.next

        self.initialize_visited()
        dfsHelper(vertex)
        print()

    def bfs(self, vertex):
        self.initialize_visited()
        self.visited[vertex] = True

        q = deque()
        q.append(vertex)

        while q:
            current_vertex = q.popleft()
            print(current_vertex, end=' ')

            temp = self.headnodes[current_vertex].next
            while temp:
                if not self.visited[temp.vertex]:
                    q.append(temp.vertex)
                    self.visited[temp.vertex] = True
                temp = temp.next

        print()

def undirectedGraph():
    mx = int(input())
    ug = Graph(mx)
    n = int(input())
    
    for _ in range(n):
        v1, v2 = map(int, input().split())
        
        if not ug.vertexExists(v1):
            ug.addVertex(v1)
        ug.addEdge(v1, v2)
        
        if not ug.vertexExists(v2):
            ug.addVertex(v2)
        ug.addEdge(v2, v1)
    
    ug.printGraph()

undirectedGraph()

