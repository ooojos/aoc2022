def aoc1():
    print("Hello World")
    with open('input1.txt', 'r') as file:
        total = 0
        listofelves = []
        for line in file:
            if line in ['\n', '\r\n']:
                listofelves.append(total)
                total = 0
            else:
                total = total + int(line)
        listofelves.sort()
        print(listofelves[-1])
        print(listofelves[-1]+listofelves[-2]+listofelves[-3])

def nicesoln():
    with open("input1.txt", "r") as file:  
        data = sorted(sum(int(y) for y in x.splitlines()) for x in file.read().split("\n\n"))
        print(data[-1])
        print(sum(data[-3:]))


aoc1()
