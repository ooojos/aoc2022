def aoc6():
    with open("in6.txt") as f:
        m = f.readline()
        print([len(set(m[i:i+4])) for i in range(len(m)-4)].index(4) + 4)
        print([len(set(m[i:i+14])) for i in range(len(m)-14)].index(14) + 14)
aoc6()
