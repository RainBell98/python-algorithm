T = int(input())
for i in range(T):
    n,k = map(int,input().split())
    p = [False]*(n+1)
    bad = []
    arr = list(map(int,input().split()))
    for j in range(len(arr)):
        p[arr[j]]= True
    for j in range(len(p)):
        if p[j] == False:
            bad.append(j)
    bad.remove(bad[0])
    print("#{}".format(i+1),end=" ")
    for j in range(len(bad)):
        print(bad[j],end=" ")
    print()


