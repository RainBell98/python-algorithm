for i in range(10):
    T = int(input())
    p = [list(map(int,input().split()))for _ in range(100)]
    MAX = []
    for j in range(100):
        res1 = 0
        for k in range(100):
            res1 += p[j][k]
            MAX.append(res1)

    for j in range(100):
        res2 = 0
        for k in range(100):
            res2 += p[k][j]
            MAX.append(res2)
    for j in range(100):
        res3 = 0
        res4 = 0
        res3 += p[j][j]
        res4 += p[j][99-i]
        MAX.append(res3)
        MAX.append(res4)



    print("#{}".format(T),max(MAX))