from collections import deque

class GraphNode:
    def __init__(self, vertex=0, next_node=None):
        self.vertex = vertex # Vertex identifier
        self.next = next_node 

class Graph:
    MAX = 10 # Maximum number of vertices
    def __init__(self):
        self.headnodes = [None] * self.MAX # Array of head nodes for
        self.n = 0 # Number of vertices in the graph
        self.visited = [False] * self.MAX # Visited flag for each
    
    def initialize_visited(self):
        self.visited = [False] * self.MAX 
    
    def addVertex(self, vertex): # Add a vertex to the graph
        if self.n+1 < self.MAX:
            self.headnodes[self.n] = GraphNode(vertex)
            self.n += 1
        else:
            print('Graph full')

    def removeVertex(self, vertex): 
        for node in self.headnodes:
            temp = node
            while temp:
                if temp.next and temp.next.vertex == vertex:
                    temp.next = temp.next.next
                    break
                temp  = temp.next
        self.headnodes[vertex] = None
        print(f'Removed vertex {vertex} from graph')

    def addEdge(self, vertex1, vertex2): 
        current = self.headnodes[vertex1]
        if current:
            while current.next:
                current = current.next
            current.next = GraphNode(vertex2)

    def removeEdge(self, vertex1, vertex2): 
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
    
        return self.headnodes[vertex] is not None

    def printGraph(self): 
        for i in range(self.MAX):
            if self.headnodes[i] is not None:
                print(f"Vertex {i}:", end="")
                curr = self.headnodes[i].next
                while curr is not None:
                    print(f" {curr.vertex}", end=", ")
                    curr = curr.next
                print()
    
    def dfs(self, vertex): 
        def dfsHelper(v):
            self.visited[v] = True
            print(v, end=' ')

            temp = self.headnodes[v]
            while temp:
                if not self.visited[temp.vertex]:
                    dfsHelper(temp.vertex)
                temp = temp.next
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

            temp = self.headnodes[current_vertex]
            while temp:
                if not self.visited[temp.vertex]:
                    q.append(temp.vertex)
                    self.visited[temp.vertex] = True
                temp = temp.next

        print()


g = Graph()
# Add vertices
for i in range(6):
    g.addVertex(i)
# Add edges
g.addEdge(0, 1)
g.addEdge(0, 3)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(1, 5)
g.addEdge(3, 4)
g.addEdge(4, 2)
g.addEdge(4, 5)
g.addEdge(5, 1)
# # Print the graph
g.printGraph()
print()
# g.removeVertex(1)
# g.removeEdge(1,5)
g.printGraph()

# # Perform DFS and BFS traversals
print("DFS starting from vertex 0:")
g.dfs(0)
g.initialize_visited()

print("BFS starting from vertex 0:")
g.bfs(1)
