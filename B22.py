N,M = map(int,input().split())
a = list(map(int, input().split()))
p = []

for i in range(len(a)-2):
    for j in range(i+1,len(a)-1):
        for k in range(j+1,len(a)):
            if a[i]+a[j]+a[k]>M:
                continue
            else:
                p.append(a[i]+a[j]+a[k])

print(max(p))
