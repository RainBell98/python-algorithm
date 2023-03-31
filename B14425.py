n,m = map(int,input().split())
p =[]
s =[]
for _ in range(n):
    p.append(str(input()))
for _ in range(m):
    s.append(str(input()))
cnt = 0
for i in s:
    if i in p:
        cnt += 1

print(cnt)