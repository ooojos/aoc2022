def aoc9():
    with open("in9.txt") as f:
        coords = {"x0y0"}
        coordsp1 = {"x0y0"}
        pozzes = [[0,0] for i in range(10)]
        for line in f:
            direction = line.split()[0].strip()
            steps = int(line.split()[1].strip())
            
            for i in range(steps):
                #print(pozzes)
                if direction == "U":
                    pozzes[0][1] -= 1
                elif direction == "D":
                    pozzes[0][1] += 1

                elif direction == "L":
                    pozzes[0][0] -= 1
                elif direction == "R":
                    pozzes[0][0] += 1
                for i in range(1, len(pozzes)):
                    if pozzes[i-1][0] - pozzes[i][0] == 2:
                        pozzes[i][0]+=1
                        if pozzes[i-1][1] == pozzes[i][1] + 1 or pozzes[i-1][1] == pozzes[i][1] + 2:
                            pozzes[i][1]+=1
                        if pozzes[i-1][1] == pozzes[i][1] - 1 or pozzes[i-1][1] == pozzes[i][1] - 2:
                            pozzes[i][1]-=1
                    elif pozzes[i-1][0] - pozzes[i][0] == -2:
                        pozzes[i][0]-=1
                        if pozzes[i-1][1] == pozzes[i][1] + 1 or pozzes[i-1][1] == pozzes[i][1] + 2:
                            pozzes[i][1]+=1
                        if pozzes[i-1][1] == pozzes[i][1] - 1 or pozzes[i-1][1] == pozzes[i][1] - 2:
                            pozzes[i][1]-=1
                    elif pozzes[i-1][1] - pozzes[i][1] == -2:
                        pozzes[i][1]-=1
                        if pozzes[i-1][0] == pozzes[i][0] + 1 or pozzes[i-1][0] == pozzes[i][0] + 2:
                            pozzes[i][0]+=1
                        if pozzes[i-1][0] == pozzes[i][0] - 1 or pozzes[i-1][0] == pozzes[i][0] - 2:
                            pozzes[i][0]-=1
                    elif pozzes[i-1][1] - pozzes[i][1] == 2:
                        pozzes[i][1]+=1
                        if pozzes[i-1][0] == pozzes[i][0] + 1 or pozzes[i-1][0] == pozzes[i][0] + 2:
                            pozzes[i][0]+=1
                        if pozzes[i-1][0] == pozzes[i][0] - 1 or pozzes[i-1][0] == pozzes[i][0] - 2:
                            pozzes[i][0]-=1
                coords.add("x"+str(pozzes[9][0])+"y"+str(pozzes[9][1]))       
                coordsp1.add("x"+str(pozzes[1][0])+"y"+str(pozzes[1][1]))
        print(len(coordsp1))
        print(len(coords))
aoc9()
