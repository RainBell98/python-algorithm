T = int(input())
for i in range(T):
    D,L,N = map(int,input().split())
    res = 0
    for j in range(N):
        res += D*(1+j*L/100)
    print("#{}".format(i+1),int(res))