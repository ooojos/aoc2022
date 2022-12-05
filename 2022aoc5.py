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
