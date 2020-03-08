def equalsWhenOneCharRemoved(x, y):
    if x == None or y == None or len(x) == len(y) or len(x)+1 < len(y) or len(y)+1 < len(x): 
        return False
    if len(x) < len(y):
        temp = x
        x = y
        y = temp
    allowedOnce = True
    j = 0
    for i in range(len(x)):
        if j < len(y) and x[i] != y[j]:
            if not allowedOnce:
                return False
            allowedOnce = False
            continue
        j+=1
    return True

print(equalsWhenOneCharRemoved("AB","A"))
