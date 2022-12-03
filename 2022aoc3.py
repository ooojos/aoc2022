def aoc3():
    with open("aoc3.txt") as f:
        total = 0
        for line in f:
            comp1 = sorted(line[:len(line)//2].strip())
            comp2 = sorted(line[len(line)//2:].strip())
            notfound = True

            comp1i = []
            comp2i = []
            for i in range(len(comp1)):
                if ord(comp1[i]) > 90:
                    comp1i.append(ord(comp1[i])-96)
                else:
                    comp1i.append(ord(comp1[i])-38)
                if ord(comp2[i]) > 90:
                    comp2i.append(ord(comp2[i])-96)
                else:
                    comp2i.append(ord(comp2[i])-38)
                    
            comp1i.sort()
            comp2i.sort()
            
            i1 = 0
            i2 = 0
            curr1 = comp1i[i1]
            curr2 = comp2i[i2]
            if curr1 == curr2:
                notfound = False
                if curr1 > 90:
                    total = total + curr1
                else:
                    total = total + curr1

            elif curr1 > curr2:
                i2 = i2 + 1
                curr2 = comp2i[i2]
            elif curr2 > curr1:
                i1 = i1 + 1
                curr1 = comp1i[i1]
            while notfound:
                
                if curr1 == curr2:
                    notfound = False
                    if curr1 > 90:
                        total = total + curr1
                    else:
                        total = total + curr2
                elif curr1 > curr2:
                    i2 = i2 + 1
                    curr2= comp2i[i2]
                elif curr2 > curr1:
                    i1 = i1 + 1
                    curr1=comp1i[i1]
        print(total)

def aoc32():
    with open("aoc3.txt") as f:
        total = 0
        for i in range(100):
            comp1 = sorted(f.readline().strip())
            comp2 = sorted(f.readline().strip())
            comp3 = sorted(f.readline().strip())
            notfound = True

            comp1i = []
            comp2i = []
            comp3i = []
            for i in range(len(comp1)):
                if ord(comp1[i]) > 90:
                    comp1i.append(ord(comp1[i])-96)
                else:
                    comp1i.append(ord(comp1[i])-38)
            for i in range(len(comp2)):
                if ord(comp2[i]) > 90:
                    comp2i.append(ord(comp2[i])-96)
                else:
                    comp2i.append(ord(comp2[i])-38)
            for i in range(len(comp3)):
                if ord(comp3[i]) > 90:
                    comp3i.append(ord(comp3[i])-96)
                else:
                    comp3i.append(ord(comp3[i])-38)                    
            comp1i.sort()
            comp2i.sort()
            comp3i.sort()
            
            i1 = 0
            i2 = 0
            i3 = 0
            curr1 = comp1i[i1]
            curr2 = comp2i[i2]
            curr3 = comp3i[i3]

            if curr1 == curr2 and curr1 == curr3:
                notfound = False
                total = total + curr1

            elif curr1 >= curr2 and curr3 >= curr2:
                i2 = i2 + 1
                curr2 = comp2i[i2]
            elif curr2 >= curr1 and curr3 >= curr1:
                i1 = i1 + 1
                curr1 = comp1i[i1]
            elif curr1 >= curr3 and curr2 >= curr3:
                i3 = i3 + 1
                curr3 = comp3i[i3]
            while notfound:
                if curr1 == curr2 and curr1 == curr3:
                    notfound = False
                    total = total + curr1
                    break

                elif curr1 >= curr2 and curr3 >= curr2:
                    i2 = i2 + 1
                    curr2 = comp2i[i2]
                elif curr2 >= curr1 and curr3 >= curr1:
                    i1 = i1 + 1
                    curr1 = comp1i[i1]
                elif curr1 >= curr3 and curr2 >= curr3:
                    i3 = i3 + 1
                    curr3 = comp3i[i3]
        print(total)


from string import ascii_letters
def goodsoln():
    scores = dict([(j, i+1)for i, j in enumerate(ascii_letters)])
    with open("aoc3.txt", 'r') as f: 
        lines = [i.strip() for i in f.readlines()] 
        # PART 1 
        total = 0 
        for line in lines: 
            a = (set(line[:len(line)//2]) & set(line[len(line)//2:])).pop()
            total += scores[a] 
        print(f"1) Total score: {total}") 
        # PART 2 
        total = 0 
        for l1, l2, l3 in zip(lines[::3], lines[1::3], lines[2::3]):
            common = (set(l1) & set(l2) & set(l3)).pop() 
            total += scores[common] 
    print(f"2) Total score: {total}")
    
goodsoln()
aoc3()
aoc32()
