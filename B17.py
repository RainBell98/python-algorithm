n = int(input())
a = []

for _ in range(n):
    a.append(list(input().split()))
a.sort(key=lambda b:int(b[0]))

for i in range(n):
    print(a[i][0],a[i][1])

