import math
T = int(input())
for i in range(T):
    a,b = map(int,input().split())
    cnt = 0
    for j in range(a,b+1):
        p = math.sqrt(j)
        if p%1>0:
            continue
        p = str(int(p))
        j = str(j)
        if p == p[::-1]and j==j[::-1]:
            cnt+=1
    print("#{}".format(i+1),cnt)



