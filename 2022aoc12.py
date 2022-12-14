from collections import deque

def bfs(maze, pos, part):
    AB = "abcdefghijklmnopqrstuvwxyz"
    w, h = len(maze[0]), len(maze)
    q = deque([[pos]])
    seen = set([pos])
    if part == 2:
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == "a":
                    q.append([(j, i)])
    while q:
        path = q.popleft()
        x, y = path[-1]
        if maze[y][x] == "E":
            return path
        if maze[y][x] == "S":
            currheight = 0
        elif maze[y][x] == "E":
            currheight = 25
        else:    
            currheight = AB.index(maze[y][x])
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < w and 0 <= y2 < h and (x2, y2) not in seen:
                if maze[y2][x2] == "S":
                    possheight = 0
                elif maze[y2][x2] == "E":
                    possheight = 25
                else:    
                    possheight = AB.index(maze[y2][x2])
                if possheight <= currheight + 1:
                    q.append(path + [(x2, y2)])
                    seen.add((x2, y2))

def aoc12():
    with open("in12.txt") as f:
        maze = []
        for line in f:
            maze.append(list(line.strip())) 
        Sy = len(maze)//2
        Sx = 0
        Ey = len(maze)//2
        Ex = len(maze[0])-25
        #print(Sy, Sx, Ey, Ex)
        maze[Sy][Sx] = "a"
        path = bfs(maze, (Sx, Sy), 1)
        print(len(path)-1)
        path2 = bfs(maze, (Sx, Sy), 2)
        print(len(path2)-1)

aoc12()
