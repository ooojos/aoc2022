import json

def aoc13():
    with open("in13.txt") as f:
        text = f.read().split("\n\n")
#        print(text[-1])

        counter = 1
        indexes = []
        messages = []
        for i in text:
            a,b = i.strip().split("\n")
            a = json.loads(a)
            b=json.loads(b)
            messages.append(a)
            messages.append(b)
            if compare(a,b):
                indexes.append(counter)
            counter+=1
        total = 0
        for i in indexes:
            total +=i
        print(total)

        messages.append(json.loads("[[2]]"))
        messages.append(json.loads("[[6]]"))
        
        for i in range(197):
            for j in range(len(messages)-1):
                if not compare(messages[j], messages[j+1]):
                    tmp = messages[j]
                    messages[j] = messages[j+1]
                    messages[j+1] = tmp
        print((messages.index([[2]])+1)*(messages.index([[6]])+1))

def compare(a, b):
    #print(a, b)
    if type(a) == int and type(b) == int:
        if a < b:
            return True
        elif b < a:
            return False
        elif a == b:
            return
    if type(a) == list and type(b) == list:
        if len(a) == 0 and len(b) != 0:
            return True
        elif len(b) == 0 and len(a) != 0:
            return False
        else:
            for i in range(max(len(a), len(b))):
                if i > len(a) - 1:
                    return True
                if i > len(b) - 1:
                    return False
                x = compare(a[i], b[i])
                if x is True:
                    return x
                if x is False:
                    return x
    if type(a) == int and type(b) == list:
        return compare([a], b)
    if type(a) == list and type(b) == int:
        return compare(a, [b])


aoc13()
