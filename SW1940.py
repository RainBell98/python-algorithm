N = int(input())
for i in range(N):
    T = int(input())
    v = 0
    v1 = 0
    for j in range(T):
        d = list(map(int,input().split()))
        if (d[0] == 1):
            v += d[1]
        elif (d[0] == 2):
            v -= 1
            if v <= 0:
                v = 0

        v1 += v
    print("#{}".format(i+1),v1)

