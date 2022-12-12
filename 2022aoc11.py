def aoc11():   
    mh = [[85, 79, 63, 72], [53, 94, 65, 81, 93, 73, 57, 92], [62, 63], [57, 92, 56], [67], [85, 56, 66, 72, 57, 99], [86, 65, 98, 97, 69], [87, 68, 92, 66, 91, 50, 68]]
    mi = [0,0,0,0,0,0,0,0]

    for i in range(10000):
        for j in range(len(mh)):
            k=0
            while len(mh[j]) > 0:
                mi[j] += 1
                if j == 0:
                    a = mh[j][0]
                    mh[j].pop(0)
                    a = a * 17
                    a = a % 9699690
                    if a % 2 == 0:
                        mh[2].append(a)
                    else:
                        mh[6].append(a)
                if j == 1:
                    a = mh[j][0]
                    mh[j].pop(0)
                    a = a * a
                    a = a % 9699690
                    if a % 7 == 0:
                        mh[0].append(a)
                    else:
                        mh[2].append(a)
                if j == 2:
                    a = mh[j][0]
                    mh[j].pop(0)
                    a = a + 7
                    a = a % 9699690
                    if a % 13 == 0:
                        mh[7].append(a)
                    else:
                        mh[6].append(a)
                if j == 3:
                    a = mh[j][0]
                    mh[j].pop(0)
                    a = a + 4
                    a = a % 9699690
                    if a % 5 == 0:
                        mh[4].append(a)
                    else:
                        mh[5].append(a)    
                if j == 4:
                    a = mh[j][0]
                    mh[j].pop(0)
                    a = a + 5
                    a = a % 9699690
                    if a % 3 == 0:
                        mh[1].append(a)
                    else:
                        mh[5].append(a)
                if j == 5:
                    a = mh[j][0]
                    mh[j].pop(0)
                    a = a + 6
                    a = a % 9699690
                    if a % 19 == 0:
                        mh[1].append(a)
                    else:
                        mh[0].append(a)
                if j == 6:
                    a = mh[j][0]
                    mh[j].pop(0)
                    a = a * 13
                    a = a % 9699690
                    if a % 11 == 0:
                        mh[3].append(a)
                    else:
                        mh[7].append(a)
                if j == 7:
                    a = mh[j][0]
                    mh[j].pop(0)
                    a = a + 2
                    a = a % 9699690
                    if a % 17 == 0:
                        mh[4].append(a)
                    else:
                        mh[3].append(a)
                k+=1
        print(str(i) + ": "+str(mi))
        #print(mh)
    #print(mh)
    print(sorted(mi)[6]*sorted(mi)[7])

aoc11()
