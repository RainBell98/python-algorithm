T = int(input())
for i in range(T):
    n,k = map(int,input().split())
    p = [False]*(n+1)

    for j in range(k):
        a = list(map(int,input().split()))

        for l in range(1,n+1):
            try:
                p[a[l-1]] = True
            except:
                continue
        for l in range(1,n+1):
            if p[l] == False:
                try:
                    print((p.index(l))+1)
                except:
                    continue
        break




