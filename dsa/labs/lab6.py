def solve_maze(maze):
    def find_path(x, y, current_path):
        x_range = len(maze)
        y_range = len(maze[0])
        if not (0 <= x < x_range and 0 <= y < y_range) or maze[x][y] == '*' or visited[x][y]:
            return False
        
        current_path.append((x, y))
        visited[x][y] = True

        current = maze[x][y]
        if current == 'T':
            return True
        
        if (find_path(x + 1, y, current_path) or 
            find_path(x - 1, y, current_path) or
            find_path(x, y + 1, current_path) or 
            find_path(x, y - 1, current_path)):
            return True
        
        current_path.pop()
        return False
    
    visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]

    for i in range(len(maze)):
        for j in range(len(maze)):
            if maze[i][j] == 'P':
                start_x = i
                start_y = j
    
    path = []
    if find_path(start_x, start_y, path):
        return "Solved", path
    else:
        return "Unsolved", []

# Driver
maze = [
[" ", "*", " ", "*", " ", " "],
[" ", "*", " ", "*", " ", " "],
["P", " ", " ", " ", "*", " "],
["*", " ", "*", "*", "*", " "],
[" ", " ", " ", " ", "*", "T"],
["*", " ", " ", " ", " ", " "]
]

status, path = solve_maze(maze)
print(status)
if status == "Solved":
    print("Path:", path)

maze = [
[" ", "*", " ", "*", " ", " "],
[" ", "*", " ", "*", " ", " "],
["P", " ", " ", " ", "*", " "],
["*", " ", "*", "*", "*", " "],
[" ", " ", " ", " ", "*", "T"],
["*", " ", " ", " ", " ", "*"]
]
status, path = solve_maze(maze)
print(status)
if status == "Solved":
    print("Path:", path)