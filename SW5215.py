
T = int(input())
for i in range(T):
    n,l = map(int,input().split())
    p = []
    for _ in range(n):
        a,b = map(int,input().split())
        p.append((a,b))
    res = [[]for _ in range(n)]
    for j in range(n):
        res[j].append(p[j])
        for k in range(0,j):
            for m in res[k]:
                a,b = m
                if b+p[j][1]<=l:
                    res[j].append((a+p[j][0],b+p[j][1]))
    MAX = 0
    for j in range(n):
        for k in res[j]:
            a,b = k
            if a>MAX:
                MAX = a
    print("#{}".format(i+1),MAX)
