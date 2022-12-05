import re

def aoc51():
    sarray = []
    sarray.append(["T","P","Z","C","S","L","Q","N"])
    sarray.append(["L","P","T","V","H","C","G"])
    sarray.append(["D","C","Z","F"])
    sarray.append(["G","W","T","D","L","M","V","C"])
    sarray.append(["P","W","C"])
    sarray.append(["P","F","J","D","C","T","S","Z"])
    sarray.append(["V","W","G","B","D"])
    sarray.append(["N","J","S","Q","H","W"])
    sarray.append(["R","C","Q","F","S","L","V"])
    with open("in5.txt") as f:
        for line in f:
            a = re.findall(r'\d+',line)
            for i in range(int(a[0])):
                try:
                    sarray[int(a[2])-1].append(sarray[int(a[1])-1].pop())
                except:
                    pass
        for i in range(10):
            try:
                print(sarray[i].pop(), end="")
            except:
                pass
        print()

def aoc52():
    sarray = []
    sarray.append(["T","P","Z","C","S","L","Q","N"])
    sarray.append(["L","P","T","V","H","C","G"])
    sarray.append(["D","C","Z","F"])
    sarray.append(["G","W","T","D","L","M","V","C"])
    sarray.append(["P","W","C"])
    sarray.append(["P","F","J","D","C","T","S","Z"])
    sarray.append(["V","W","G","B","D"])
    sarray.append(["N","J","S","Q","H","W"])
    sarray.append(["R","C","Q","F","S","L","V"])
    with open("in5.txt") as f:
        for line in f:
            a = re.findall(r'\d+',line)
            tmp = []
            for i in range(int(a[0])):
                try:
                    tmp.append(sarray[int(a[1])-1].pop())
                except:
                    pass
            for i in range(int(a[0])):
                try:
                    sarray[int(a[2])-1].append(tmp.pop())
                except:
                    pass
        for i in range(10):
            try:
                print(sarray[i].pop(), end="")
            except:
                pass
aoc51()
aoc52()


carg, ins = [s.split('\n') for s in open("in5.txt").read().split("\n\n")]
cargo = [[c for c in x if c!=' '][::-1] for x in map(list,zip(*[*carg])) if x[-1]!=' ']
instructions = [[int(x) for x in s if x.isdigit()] for s in ins]

def part1(cargo, instructions):
    for moves, a, b in instructions: 
        for _ in range(moves):
            cargo[b-1].append(cargo[a-1].pop())
    return ''.join(map(lambda x: x[-1], cargo))

def part2(cargo, instructions):
    for moves, a, b in instructions:
        cargo[b-1].extend(cargo[a-1][-moves:])
        del cargo[a-1][-moves:]
    return ''.join(map(lambda x: x[-1], cargo))
