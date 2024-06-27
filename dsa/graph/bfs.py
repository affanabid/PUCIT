from collections import deque

def bfs(adjList, start, visited):
    visited[start] = True

    q = deque()
    q.append(start)

    while q:
        current = q.popleft()
        print(current, end=' ')

        for neighbour in adjList[current]:
            if not visited[neighbour]:
                q.append(neighbour)
                visited[neighbour] = True

def addEdge(adjList, current, neighbour):
    adjList[current].append(neighbour)


def main():
    vertices = 5
    visited = [False] * vertices

    adjList = []
    for i in range(vertices):
        adjList.append([])

    addEdge(adjList, 0, 1)
    addEdge(adjList, 0, 2)
    addEdge(adjList, 1, 3)
    addEdge(adjList, 1, 4)
    addEdge(adjList, 2, 4)

    print(f'bfs: ', end=' ')

    bfs(adjList, 0, visited)


main()