T = int(input())
for i in range(T):
    n = int(input())
    p = list(map(int,input().split()))
    good = 0
    for j in range(len(p)-1):
        if p[j]<p[-1]:
            good += p[-1]-p[j]
    print(good)