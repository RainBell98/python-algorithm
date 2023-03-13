cnt = int(input())
p = list(map(int,input().split()))

p.sort()
temp1 = 0

for i in range(1,cnt+1):
    temp1 += sum(p[0:i])

print(temp1)
