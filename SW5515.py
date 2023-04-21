T = int(input())
for i in range(T):
    m,d = map(int,input().split())
    day = 0
    res = 0
    if m == 2:
        day = 31
    elif m == 3:
        day = 60
    elif m == 4:
        day = 91
    elif m == 5:
        day = 121
    elif m == 6:
        day = 152
    elif m == 7:
        day = 182
    elif m == 8:
        day = 213
    elif m == 9:
        day = 244
    elif m == 10:
        day = 274
    elif m == 11:
        day = 305
    elif m == 12:
        day = 335
    else:
        pass
    day += d
    if day%7 == 1:
        res = 4
    elif day%7 == 0:
        res = 3
    elif day%7 == 6:
        res = 2
    elif day%7 == 5:
        res = 1
    elif day%7 == 4:
        res = 0
    elif day%7 == 3:
        res = 6
    elif day%7 == 2:
        res = 5
    print("#{}".format(i+1),res)


