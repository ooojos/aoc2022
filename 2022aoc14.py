def aoc14():
    with open("in14.txt") as f:
        walls = set()
        for line in f:
            wallcorners = line.strip().split("->")
            for i in range(len(wallcorners)-1):
                startx = int(wallcorners[i].split(",")[0])
                starty = int(wallcorners[i].split(",")[1])
                endx = int(wallcorners[i+1].split(",")[0])
                endy = int(wallcorners[i+1].split(",")[1])
                x = startx
                y = starty
                walls.add((endx, endy))
                
                while x != endx or y != endy:
                    wall = (x,y)
                    walls.add(wall)
                    if x == endx and y < endy:
                        y+=1
                    elif x== endx and y > endy:
                        y-=1
                    elif x < endx and y == endy:
                        x+=1
                    elif x > endx and y == endy:
                        x-=1
                        
        deepest = 0
        for i in walls:
            if i[1] > deepest:
                deepest = i[1]
        
        counter = 0
        currx = 500
        curry = 0
        while curry < 158:
            if not ((currx, curry) in walls):
                if not ((currx, curry+1) in walls):
                    curry+=1
                elif not ((currx-1, curry+1) in walls):
                    currx -=1
                    curry +=1
                elif not ((currx+1, curry+1) in walls):
                    currx +=1
                    curry +=1
                else:
                    walls.add((currx, curry))
                    counter+=1
                    currx = 500
                    curry = 0
        print(counter)
        for i in range(600):
            walls.add((200+i,deepest+2))
        
        currx = 500
        curry = 0
        backatsource = False
        while not backatsource:
            if not ((currx, curry) in walls):
                if not ((currx, curry+1) in walls):
                    curry+=1
                elif not ((currx-1, curry+1) in walls):
                    currx -=1
                    curry +=1
                elif not ((currx+1, curry+1) in walls):
                    currx +=1
                    curry +=1
                else:
                    if currx == 500 and curry == 0:
                        counter+=1
                        walls.add((currx, curry))
                        backatsource = True
                    else:
                        walls.add((currx, curry))
                        counter+=1
                        currx = 500
                        curry = 0
        print(counter)


def printgrid(walls):     
    y = 0
    x = 487
    while y < 12:
        x = 487
        while x < 514:
            if(x,y) in walls:
                print("#", end="")
            else:
                print(".", end="")
            x+=1
        print()
        y+=1
                        
                        
aoc14()
