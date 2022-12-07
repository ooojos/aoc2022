def aoc7():
    with open("in7.txt") as f:
        dirs = [["/", 0]]
        cwd = "/"
        for line in f:
            if line[0:3] == "dir":
                dirs.append([cwd+line[4:].strip(), 0])
            elif line[0:4] == "$ cd":
                if line[5] == "/":
                    pass
                elif line[5:7] == "..":
                    cwd = cwd[0:cwd.rindex("/")]
                    cwd = cwd[0:cwd.rindex("/")+1]
                else:
                    cwd = cwd+line[5:].strip()+"/"
            elif line[0:4] == "$ ls":
                pass
            else:
                size = int(line.split()[0])
                dirs[0][1]+=size
                tcwd = cwd
                while len(tcwd) > 1:
                    for i in range(len(dirs)):
                        if dirs[i][0] == tcwd:
                            dirs[i][1] += size
                    tcwd = tcwd[0:tcwd.rindex("/")]
        total = 0
        freespace = 70000000-dirs[0][1]
        spaceneeded = 30000000-freespace
        target = 0;
        for i in range(len(dirs)):
            if dirs[i][1] < 100000:
                total += dirs[i][1]
            if dirs[i][1] > spaceneeded and dirs[i][1] < dirs[target][1]:
                target = i
        print(total)
        print(dirs[target][1])
aoc7()

from collections import defaultdict
from itertools import accumulate

def goodsoln():
    dirs = defaultdict(int)

    for line in open('in7.txt'):
        match line.split():
            case '$', 'cd', '/': curr = ['']
            case '$', 'cd', '..': curr.pop()
            case '$', 'cd', x: curr.append(x+'/')
            case '$', 'ls': pass
            case 'dir', _: pass
            case size, _:
                for p in accumulate(curr):
                    dirs[p] += int(size)

    print(sum(s for s in dirs.values() if s <= 100_000))
    print(min(s for s in dirs.values() if s >= dirs[''] - 40_000_000))
goodsoln()
