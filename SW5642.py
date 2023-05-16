T = int(input())
for i in range(T):
    n = int(input())
    p = list(map(int, input().split()))
    k = []
    for j in range(len(p)):
        res = 0
        for s in range(j, len(p)):
            res += p[s]
            k.append(res)


    print("#{}".format(i+1),max(k))

