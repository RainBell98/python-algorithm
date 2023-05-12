T = int(input())
for i in range(T):
    n,m,k = map(int,input().split())
    N = list(map(int,input().split()))
    boong = True
    for j in range(len(N)):
        if N[j]>=m:
            boong = True
        else:
            boong = False
            break
    if boong == True:
        print("Possible")
    else:
        print("Impossible")

