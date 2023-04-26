T = int(input())
for i in range(T):
    tc = int(input())
    p = list(map(int,input().split()))
    res = 0
    a=[]
    for j in range(len(p)-1):
        res = p[j]-p[j+1]
        if res<0:
            res = res*(-1)
        a.append(res)
    print("#{}".format(i+1),max(a))