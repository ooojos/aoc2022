def aoc1():
    print("Hello World")
    maxcals = [0,0,0]
    with open('input1.txt') as openfileobject:
        total = 0
        for line in openfileobject:
            if line in ['\n', '\r\n']:
                total = 0
            else:
                total = total + int(line)
            if total > maxcals[2] and total < maxcals[1]:
                maxcals[2] = total
            if total > maxcals[1] and total < maxcals[0]:
                maxcals[2] = maxcals[1]
                maxcals[1] = total
            if total > maxcals[0]:
                maxcals[2] = maxcals[1]
                maxcals[1] = maxcals[0]
                maxcals[0] = total
        print(maxcals[0] + maxcals[1] + maxcals[2])

aoc1()
