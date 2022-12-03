def aoc2():
    with open("aoc21.txt") as f:
        total1 = 0
        total2 = 0
        scoresdict = {"A X": 4,"A Y": 8,"A Z": 3, "B X" : 1, "B Y": 5 ,"B Z": 9, "C X": 7, "C Y" : 2, "C Z": 6}
        scores2dict = {"A X": 3,"A Y": 4,"A Z": 8, "B X" : 1, "B Y": 5 ,"B Z": 9, "C X": 2, "C Y" : 6, "C Z": 7}
        for line in f:
            total1 = total1 + scoresdict[line.strip()]
            total2 = total2 + scores2dict[line.strip()]
        print(total1)
        print(total2)
        
aoc2()
