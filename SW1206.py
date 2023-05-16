T = int(input())
for i in range(T):
    p = list(map(int,input().split()))
    cnt = 0
    for j in range(2,len(p)-2):
        k = []
        if p[j]>p[j+1] and p[j]>p[j-1] and p[j]>p[j-2] and p[j]>p[j+2]:
           k.append(p[j+1])
           k.append(p[j+2])
           k.append(p[j-1])
           k.append(p[j-2])
           MAX = max(k)
           cnt += p[j]-MAX
    print(cnt)

