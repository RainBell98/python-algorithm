N = int(input())
res = 0
for i in range(1,N+1):
    p = map(int,input().split())
    for j in p:
        if j % 2 == 0:
            res -= j
        else:
            res += j
    print("#"+str(i),res)
