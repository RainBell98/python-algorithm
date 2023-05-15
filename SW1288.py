N = int(input())
for i in range(N):
    cnt = input()
    p = []
    res = ''
    k = []
    m=int(cnt)
    s=0
    n = -1
    while len(k) != 10:
        res = list(cnt)
        for j in range(len(res)):
            p.append(res[j])
        for j in p:
            if j not in k:
                k.append(j)
        s += m
        cnt = str(s)
        n +=1


    print("#{}".format(i+1),n*m)


