def aoc4():
    with open("aoc4.txt") as f:
        total1 = 0
        total2 = 0
        for line in f:
            a = line.strip().replace("-",",").split(",")
            a = [int(i) for i in a]
            if (a[0] <= a[2] and a[1] >= a[3]) or (a[0] >= a[2] and a[1] <= a[3]):
                total1 = total1 + 1
            if not (a[1] < a[2] or a[0] > a[3]):
                total2 = total2 + 1
        print(total1)
        print(total2)

aoc4()
