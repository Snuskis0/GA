def howManyTrueIn(list):
    count = 0
    for item in list:
        if item:
            count += 1
    return count

def addPos(pos1, pos2):
    x1 = pos1[0]
    y1 = pos1[1]
    x2 = pos2[0]
    y2 = pos2[1]
    return (x1+x2,y1+y2)

def subPos(pos1, pos2):
    x1 = pos1[0]
    y1 = pos1[1]
    x2 = pos2[0]
    y2 = pos2[1]
    return (x1-x2,y1-y2)

def multiplyPos(pos, factor):
    print("Lucas är dum i huvet")
    return ((pos[0]*factor, pos[1]*factor))

def reverseTuple(tuple):
    (x, y) = tuple
    return (-x, -y)

def reverseXInTuple(tuple):
    (x, y) = tuple
    return (-x, y)