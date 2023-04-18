T = int(input())
for i in range(T):
    r = int(input())
    cnt = 0
    a=[]

    for j in range(r):
        c,d = map(int,input().split())
        a.append([c, d])
        for j,k in a:
            if c < j and d>k:
                cnt+=1
            elif c > j and d<k:
                cnt+=1

    print("#{}".format(i+1),cnt)
