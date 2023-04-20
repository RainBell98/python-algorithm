T = int(input())
def MAx(ls):
    a= []
    b =[]
    MAX = max(ls)
    MAX_in = ls.index(MAX)
    b = ls
    a = ls
    a.sort(reverse=True)
    if MAX == b[0]:
        MAX = a[1]
        MAX_in = b.index(a[1])
        temp = b[1]
        b[1] = MAX
        b[MAX_in] = temp
    elif MAx != b[0]:
        temp = b[0]
        b[0] = MAX
        b[MAX_in] = temp
    return b
def MIn(ls):
    MIN = min(ls)
    MIN_in = ls.index(MIN)
    a = ls
    a.sort()
    if MIN != 0:
        if MIN == ls[0]:
            for i in range(1, len(a)):
                if a[i] != 1:
                    MIN = a[i]
                    MIN_in = ls.index(a[i])
            temp = ls[1]
            ls[1] = MIN
            ls[MIN_in] = temp
        else:
            temp = ls[0]
            ls[0] = MIN
            ls[MIN_in] = temp
    else:
        for i in range(1,len(a)):
            if a[i] != 1:
                MIN = a[i]
                MIN_in = ls.index(a[i])
        temp = ls[0]
        ls[0] = MIN
        ls[MIN_in] = temp


    return ls
for i in range(T):
    num = int(input())
    ls = list(map(int,str(num)))
    print(MIn(ls))
    #print("#{}".format(i+1),MAx(ls),MIn(ls))




