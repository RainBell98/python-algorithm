T = int(input())
for i in range(T):

    n,q = map(int,input().split())
    N = list(0 for _ in range(n))
    for j in range(1,q+1):
        l,r = map(int,input().split())
        for k in range(l-1,r):
            N[k] = j
    print("#{}".format(i+1),end=" ")
    for j in range(len(N)):
        print(N[j],end="")



