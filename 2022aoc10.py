def aoc10():
    with open("in10.txt") as f:
        x = 1
        cycle = 0
        total = 0
        lines = []
        counter = 0
        currline = ""
        for line in f:
            if counter == 40:
                lines.append(currline)
                print(currline)
                currline = ""
                counter = 0
            if line.strip() == "noop":
                cycle+=1
                counter+=1
                total+=check(x, cycle)
                if counter == x or counter == x + 1 or counter == x + 2:
                    currline+="#"
                else:
                    currline+="."
                if counter == 40:
                    lines.append(currline)
                    print(currline)
                    currline = ""
                    counter = 0
            else:
                cycle+=1
                counter+=1
                if counter == x or counter == x + 1 or counter == x + 2:
                    currline+="#"
                else:
                    currline+="."
                if counter == 40:
                    lines.append(currline)
                    print(currline)
                    currline = ""
                    counter = 0
                total+=check(x, cycle)
                cycle+=1
                counter+=1
                if counter == x or counter == x + 1 or counter == x + 2:
                    currline+="#"
                else:
                    currline+="."
                if counter == 40:
                    lines.append(currline)
                    print(currline)
                    currline = ""
                    counter = 0
                total+=check(x, cycle)
                x += int(line.split()[1].strip())
            
            
        print(total)
def check(x, cycle):
    check = [20, 60, 100, 140, 180, 220]
    if cycle in check:
        return x * cycle
    else:
        return 0
        
aoc10()
